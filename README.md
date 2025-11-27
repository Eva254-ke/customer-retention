# Customer Retention Platform

This repository now ships as a single Django application that bundles the previous microservices (user management, communications, inference, and analytics) into one hackathon-friendly codebase backed by SQLite.

## Single Entrypoint

Use `run_service.py` from the repo root to migrate the database and start the monolith:

```bash
python run_service.py --list              # shows the available target ("monolith")
python run_service.py                     # runs migrations + Django dev server on :8000
```

The script automatically sets the correct working directory and runs migrations before launching `runserver`. Ensure your virtual environment is activated and dependencies are installed via `pip install -r backend/user-service/user-service/requirements.txt`.

## Environment Variables

The Django app reads shared environment variables (e.g., `AFRICASTALKING_USERNAME`, `AFRICASTALKING_API_KEY`, `DJANGO_SECRET_KEY`). Export them in your shell prior to invoking `run_service.py`.
