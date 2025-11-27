# User Service for Retain

This is the User Service component of the Retain project, designed to manage user profiles, preferences, and authentication for transport and health startups in Kenya.

## Features

- **User Profiles**: Create, read, update, and delete user profiles.
- **Preferences Management**: Allow users to set and update their preferences.
- **Opt-in Management**: Manage user consent for communications.
- **Secure Authentication**: Implement secure user authentication and authorization.

## Technologies Used

- **Django REST Framework**: For building the RESTful API.
- **PostgreSQL**: As the database for storing user data (configuration in `settings.py`).
- **Celery**: For handling asynchronous tasks related to user notifications.
- **Docker**: For containerization of the service.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd retain/services/user-service
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   ```
   python manage.py migrate
   ```

4. **Start the Development Server**:
   ```
   python manage.py runserver
   ```

## API Endpoints

- **User Registration**: `POST /api/users/register/`
- **User Login**: `POST /api/users/login/`
- **Get User Profile**: `GET /api/users/profile/`
- **Update User Profile**: `PUT /api/users/profile/`

## Testing

To run tests, use the following command:
```
python manage.py test
```

## Deployment

This service can be deployed using Docker. Build the Docker image with:
```
docker build -t user-service .
```

Then run the container:
```
docker run -d -p 8000:8000 user-service
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.