# Waitlist Project

A Django REST API for managing a waitlist.

## Features

- Join the waitlist with name and email
- Sends confirmation email to users
- Admin interface for managing subscriptions
- Health check endpoint

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set environment variables (see `.env` below)
5. Run migrations:
   ```sh
   python manage.py migrate
   ```
6. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
7. Start the server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

- `GET /` — Health check
- `POST /join/` — Join the waitlist (`name`, `email`)

## Environment Variables

- `ADMIN_USERNAME`
- `ADMIN_EMAIL`
- `ADMIN_PASSWORD`
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `DATABASE_URL`
- `DEFAULT_FROM_EMAIL`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `CORS_ORIGIN_ALLOW_ALL`
- `CORS_ALLOWED_ORIGINS`

## License

This project is for demonstration purposes only. It is not licensed for commercial or production use.
