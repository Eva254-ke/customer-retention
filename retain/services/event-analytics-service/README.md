# Event Analytics Service

This microservice is responsible for collecting, processing, and analyzing user interaction events to predict customer churn. It serves as a crucial component in the Retain system, enabling personalized engagement strategies based on user behavior.

## Features

- **Event Collection**: Captures user interaction data from various sources.
- **Data Processing**: Preprocesses and stores event data for analysis.
- **Analytics**: Provides insights into user behavior and churn risk.

## Architecture

The Event Analytics Service is built using Python and Flask, and it follows a microservices architecture. It communicates with other services via RESTful APIs.

## Setup

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd retain/services/event-analytics-service
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the service**:
   ```
   python src/app.py
   ```

## API Endpoints

- **POST /events**: Submit a new event.
- **GET /events**: Retrieve a list of events.

## Monitoring

The service can be monitored using Prometheus and Grafana, which are set up in the infrastructure directory.

## Security

Ensure that sensitive data is handled securely and that proper authentication is enforced for API access.

## License

This project is licensed under the MIT License. See the LICENSE file for details.