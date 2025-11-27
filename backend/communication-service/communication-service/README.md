# Communication Service

This service is responsible for managing communication with users through SMS, USSD, and voice calls. It integrates with Africa's Talking SMS API to send personalized messages and handle user engagement.

## Features

- **SMS Messaging**: Send personalized SMS messages to users based on churn risk predictions.
- **USSD Surveys**: Engage users through USSD for feedback and surveys.
- **Voice Calls**: Automate voice calls for important notifications and reminders.
- **Task Queue**: Ships with a lightweight in-memory queue for background SMS delivery without Redis.

## Architecture

- **Entry Point**: The main application is set up in `src/app.py`.
- **Services**: 
  - `africas_talking.py`: Functions for interacting with the Africa's Talking API.
  - `messaging.py`: Logic for handling messaging workflows.
- **Tasks**: 
  - `in_memory_db.py`: Thread-safe key-value store plus queue utilities that replace Redis.
  - `sms_queue.py`: Handles SMS background jobs using the in-memory queue.
- **Routes**: 
  - `communications.py`: API endpoints for triggering communications.

## Setup

1. **Environment Variables**: Ensure to set up the required environment variables for API keys and other configurations.
2. **Install Dependencies**: Run `pip install -r requirements.txt` to install the necessary packages.
3. **Run the Service**: Use the command `python src/app.py` to start the communication service.

## Monitoring

Integrate with monitoring tools to track the performance and success rates of sent messages. Use logging to capture any errors or issues during message delivery.

## Compliance

Ensure compliance with local regulations regarding user consent for messaging, particularly under the Kenya Data Protection Act.
