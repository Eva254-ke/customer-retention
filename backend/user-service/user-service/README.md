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

## Sample cURL Calls

- Create user

  ```bash
  curl -X POST http://localhost:8000/api/users/ \
    -H "Content-Type: application/json" \
    -d '{
      "username": "jdoe",
      "email": "jdoe@example.com",
      "first_name": "Jane",
      "last_name": "Doe",
      "phone_number": "+254700000000"
    }'
  ```

- List users

  ```bash
  curl http://localhost:8000/api/users/
  ```

- Update preferences

  ```bash
  curl -X PATCH http://localhost:8000/api/users/1/preferences/ \
    -H "Content-Type: application/json" \
    -d '{
      "preferences": {
        "channel": "sms",
        "language": "en"
      }
    }'
  ```

- Send SMS synchronously

  ```bash
  curl -X POST http://localhost:8000/api/communications/send-sms/ \
    -H "Content-Type: application/json" \
    -d '{
      "phone_number": "+254700000000",
      "message": "Habari! Thanks for riding with us."
    }'
  ```

- Send SMS asynchronously & poll status

  ```bash
  curl -X POST http://localhost:8000/api/communications/send-sms/ \
    -H "Content-Type: application/json" \
    -d '{
      "phone_number": "+254700000000",
      "message": "Come back for a discount!",
      "async": true
    }'

  curl http://localhost:8000/api/communications/tasks/<task_id>/
  ```

- Predict churn

  ```bash
  curl -X POST http://localhost:8000/api/inference/predict/ \
    -H "Content-Type: application/json" \
    -d '{
      "user_id": "jdoe",
      "features": {
        "engagement_score": 0.3,
        "last_active_days": 14
      }
    }'
  ```

- Log an event

  ```bash
  curl -X POST http://localhost:8000/api/analytics/events/ \
    -H "Content-Type: application/json" \
    -d '{
      "event_type": "ride_completed",
      "user_id": "jdoe",
      "metadata": {
        "fare": 250
      }
    }'
  ```

- List events

  ```bash
  curl http://localhost:8000/api/analytics/events/
  ```

All commands assume the server is running on `localhost:8000` and the `.env` file contains the Africa's Talking sandbox credentials. Adjust IDs and payloads as needed.
