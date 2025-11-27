# Retain Frontend Documentation

This directory contains the frontend application for the Retain project, which is a scalable microservices-based AI assistant designed to predict customer churn and automate personalized SMS engagement for transport and health startups in Kenya.

## Project Structure

- **public/**: Contains static files, including the main HTML file.
- **src/**: Contains the source code for the React application.
  - **components/**: Contains React components for the application.
    - `Dashboard.tsx`: Component for visualizing churn statistics and managing campaigns.
    - `ChurnStats.tsx`: Component for displaying churn statistics.
    - `CampaignManager.tsx`: Component for managing campaigns.
  - **services/**: Contains API service functions for making requests to backend services.
    - `api.ts`: Functions for API calls.
  - **types/**: Contains TypeScript types and interfaces used throughout the application.
    - `index.ts`: Type definitions.
  - `App.tsx`: Main component that sets up routing and layout.
  - `index.tsx`: Entry point for the React application.
  
## Installation

To install the necessary dependencies, run:

```
npm install
```

## Running the Application

To start the development server, use:

```
npm start
```

The application will be available at `http://localhost:3000`.

## Building for Production

To build the application for production, run:

```
npm run build
```

This will create an optimized build in the `build/` directory.

## Docker

To build the Docker image for the frontend application, use the following command:

```
docker build -t retain-frontend .
```

To run the Docker container:

```
docker run -p 3000:3000 retain-frontend
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.