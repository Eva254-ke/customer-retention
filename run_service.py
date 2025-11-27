#!/usr/bin/env python3
"""
Unified entrypoint for running the monolithic backend locally.

Usage:
    python run_service.py            # runs migrations + server
    python run_service.py --list     # shows available targets (just the monolith)
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List, Sequence


BASE_DIR = Path(__file__).resolve().parent


@dataclass
class ServiceCommand:
    command: Sequence[str]
    workdir: Path
    description: str
    pre_commands: List[Sequence[str]] = field(default_factory=list)


def _python_cmd(*parts: str) -> List[str]:
    return [sys.executable, *parts]


SERVICES = {
    "monolith": ServiceCommand(
        description="Django app bundling users, communications, inference, and analytics.",
        workdir=BASE_DIR / "backend/user-service/user-service/src",
        pre_commands=[
            _python_cmd("manage.py", "migrate", "--noinput"),
        ],
        command=_python_cmd("manage.py", "runserver", "0.0.0.0:8000"),
    ),
}


def run_command(cmd: Sequence[str], workdir: Path, env: dict[str, str] | None = None) -> None:
    print(f"[run-service] {' '.join(cmd)} (cwd={workdir})")
    subprocess.run(cmd, cwd=workdir, check=True, env=env or os.environ.copy())


def serve(service_name: str) -> None:
    service = SERVICES.get(service_name)
    if not service:
        print(f"Unknown service '{service_name}'. Use --list to see available services.", file=sys.stderr)
        sys.exit(1)

    for pre_cmd in service.pre_commands:
        run_command(pre_cmd, service.workdir)

    run_command(service.command, service.workdir)


def list_services() -> None:
    print("Available services:")
    for name, svc in SERVICES.items():
        print(f"  - {name}: {svc.description}")


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the monolithic backend from a single entrypoint.")
    parser.add_argument("service", nargs="?", help="Service name to run. Defaults to monolith.")
    parser.add_argument("--list", action="store_true", help="List services and exit.")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> None:
    args = parse_args(argv)
    if args.list:
        list_services()
        return
    target = args.service or "monolith"
    serve(target)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"\nCommand failed with exit code {exc.returncode}.", file=sys.stderr)
        sys.exit(exc.returncode)
