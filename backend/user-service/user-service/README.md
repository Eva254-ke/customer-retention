# Retain Monolith

This directory hosts the unified Django project that now powers user management, communications, inference, and analytics for the hackathon.

## Setup

1. Create/activate a virtual environment.
2. Install dependencies:
   ```
   pip install -r backend/user-service/user-service/requirements.txt
   ```
3. Apply migrations and run the dev server:
   ```
   cd backend/user-service/user-service/src
   python manage.py migrate
   python manage.py runserver
   ```
   Or from the repo root:
   ```
   python run_service.py
   ```

## Key API Surfaces

- `POST /api/communications/send-sms/` – synchronous or async SMS (toggle with `{"async": true}`).
- `POST /api/inference/predict/` – lightweight churn scoring plus retention messaging.
- `GET/POST /api/analytics/events/` – log or inspect behavioral events.
- `GET/POST /api/users/` – manage users; preferences live at `/api/users/<id>/preferences/`.

All endpoints default to JSON and persist to SQLite (`db.sqlite3`). Africa's Talking credentials can be provided via `AFRICASTALKING_USERNAME` and `AFRICASTALKING_API_KEY`.
