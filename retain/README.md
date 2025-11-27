# Retain Project

Retain is a scalable microservices-based AI assistant designed to predict customer churn and automate personalized SMS engagement for transport and health startups in Kenya. This project leverages various microservices to handle user management, event analytics, AI inference, communication, and API gateway functionalities.

## Architecture Overview

- **User Service**: A Django REST Framework microservice that manages user profiles, preferences, and opt-in management. It handles secure authentication.
  
- **Event & Analytics Service**: Collects user interaction data, preprocesses it, and stores it in a dedicated database for analysis.
  
- **AI Inference Service**: Integrates with the Groq API to analyze churn risk and generate personalized retention messages using Llama-3-based prompts.
  
- **Communication Service**: Utilizes Africa’s Talking SMS API to deliver personalized SMS, conduct USSD surveys, and manage voice calls. It handles queuing and retries with Celery.
  
- **API Gateway**: Routes external and frontend requests, enforcing rate limits and security measures.

- **Frontend**: A React dashboard for administrators to visualize churn statistics, trigger campaigns, and monitor ROI metrics.

## Implementation Details

- Secure API keys and secrets using environment variables or vault services.
- Use asynchronous task queues (e.g., Celery with Redis) for background tasks such as inference and SMS sending.
- Provide RESTful APIs between microservices with proper authentication tokens.
- Design microservice-specific databases to isolate data concerns.
- Deploy using Docker containers, orchestrated with Kubernetes or AWS ECS.
- Monitor services with centralized logging (ELK) and alerting (Prometheus/Grafana).

## Sample Workflow

1. User activity streams to the Event Service.
2. Periodic batch inference by the AI Service using Groq prompts to compute churn risk.
3. Trigger the Communication Service for personalized SMS via Africa’s Talking if risk exceeds a defined threshold.
4. Admins view real-time dashboards in React to adjust campaigns.

## Security & Compliance

- Encrypt sensitive data and enforce strict access controls.
- Ensure user consent for messaging in compliance with the Kenya Data Protection Act.
- Apply rate limiting to external APIs to avoid cost overruns.

## Getting Started

To get started with the Retain project, clone the repository and follow the setup instructions in each service's README file. Ensure you have the necessary dependencies installed and configured.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.