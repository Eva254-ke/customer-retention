import logging
import threading
import time
import uuid
from collections import defaultdict, deque
from datetime import datetime
from typing import Any, Callable, Deque, Dict, Optional

logger = logging.getLogger(__name__)


class InMemoryDB:
    """Thread-safe in-memory key-value store with named collections and queues."""

    def __init__(self) -> None:
        self._storage: Dict[str, Dict[str, Any]] = defaultdict(dict)
        self._queues: Dict[str, Deque[str]] = defaultdict(deque)
        self._lock = threading.Lock()

    def set(self, collection: str, key: str, value: Dict[str, Any]) -> None:
        with self._lock:
            self._storage[collection][key] = dict(value)

    def get(self, collection: str, key: str, default: Optional[Any] = None) -> Optional[Dict[str, Any]]:
        with self._lock:
            value = self._storage.get(collection, {}).get(key, default)
            return dict(value) if isinstance(value, dict) else value

    def delete(self, collection: str, key: str) -> None:
        with self._lock:
            if collection in self._storage:
                self._storage[collection].pop(key, None)

    def list(self, collection: str) -> list[Dict[str, Any]]:
        with self._lock:
            return [dict(value) for value in self._storage.get(collection, {}).values()]

    def enqueue(self, queue_name: str, item: str) -> None:
        with self._lock:
            self._queues[queue_name].append(item)

    def dequeue(self, queue_name: str) -> Optional[str]:
        with self._lock:
            queue = self._queues.get(queue_name)
            if not queue:
                return None
            return queue.popleft() if queue else None

    def queue_length(self, queue_name: str) -> int:
        with self._lock:
            queue = self._queues.get(queue_name)
            return len(queue) if queue else 0


class SimpleTaskQueue:
    """Minimal task queue that relies on the in-memory DB instead of Redis."""

    def __init__(
        self,
        db: InMemoryDB,
        queue_name: str,
        collection: str,
        poll_interval: float = 0.2,
    ) -> None:
        self.db = db
        self.queue_name = queue_name
        self.collection = collection
        self.poll_interval = poll_interval
        self._handler: Optional[Callable[[Dict[str, Any]], None]] = None
        self._worker: Optional[threading.Thread] = None
        self._stop_event = threading.Event()

    def register_handler(self, handler: Callable[[Dict[str, Any]], None]) -> None:
        self._handler = handler

    def start(self) -> None:
        if self._handler is None:
            raise ValueError("A handler must be registered before starting the queue.")
        if self._worker and self._worker.is_alive():
            return
        self._stop_event.clear()
        self._worker = threading.Thread(target=self._run, daemon=True)
        self._worker.start()

    def stop(self) -> None:
        if not self._worker:
            return
        self._stop_event.set()
        self._worker.join(timeout=2)
        self._worker = None

    def enqueue(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        task_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        record = {
            "id": task_id,
            "payload": payload,
            "status": "queued",
            "created_at": now,
            "updated_at": now,
            "error": None,
        }
        self.db.set(self.collection, task_id, record)
        self.db.enqueue(self.queue_name, task_id)
        return record

    def get_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        return self.db.get(self.collection, task_id)

    def _update_status(self, task_id: str, status: str, error: Optional[str] = None) -> None:
        task = self.db.get(self.collection, task_id)
        if not task:
            return
        task["status"] = status
        task["error"] = error
        task["updated_at"] = datetime.utcnow().isoformat()
        self.db.set(self.collection, task_id, task)

    def _run(self) -> None:
        while not self._stop_event.is_set():
            task_id = self.db.dequeue(self.queue_name)
            if task_id is None:
                time.sleep(self.poll_interval)
                continue

            task = self.db.get(self.collection, task_id)
            if not task:
                continue

            try:
                self._update_status(task_id, "processing")
                self._handler(task["payload"])  # type: ignore[index]
                self._update_status(task_id, "completed")
            except Exception as exc:  # pragma: no cover
                logger.exception("Task %s failed: %s", task_id, exc)
                self._update_status(task_id, "failed", str(exc))
