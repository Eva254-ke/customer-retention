# AI Inference Service

This microservice is responsible for predicting customer churn and generating personalized retention messages for transport and health startups in Kenya. It leverages the Groq API for churn risk analysis and utilizes Llama-3-based prompts for message generation.

## Features

- **Churn Prediction**: Analyzes user data to predict the likelihood of churn.
- **Personalized Messaging**: Generates tailored retention messages based on churn risk.
- **Integration with Other Services**: Communicates with the Event & Analytics Service and Communication Service for a seamless user experience.

## Architecture

The AI Inference Service is structured as follows:

- **src/app.py**: Entry point for the service, setting up the application and routes.
- **src/models/churn.py**: Defines the data models used for churn prediction.
- **src/services/groq_client.py**: Contains functions for interacting with the Groq API.
- **src/services/inference.py**: Implements the logic for performing churn risk inference.
- **src/routes/predictions.py**: Defines the API routes for handling churn prediction requests.

## Setup

1. **Environment Variables**: Ensure that all necessary environment variables are set, including API keys and secrets.
2. **Dependencies**: Install the required dependencies listed in `requirements.txt`.
3. **Docker**: Build and run the service using Docker.

## Usage

- Start the service and access the prediction endpoints to analyze churn risk and generate messages.
- Integrate with the Communication Service to send personalized SMS based on the predictions.

## Security

- Ensure that sensitive data is encrypted and access controls are enforced.
- Comply with the Kenya Data Protection Act regarding user consent for messaging.

## Monitoring

Utilize centralized logging and monitoring tools to track service performance and errors.