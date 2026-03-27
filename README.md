# Gemini AI Chatbot Backend

A Django REST API backend for an AI-powered chatbot using Google Gemini AI. The application provides a RESTful API for storing and managing chat conversations.

## Features

- **REST API**: Full CRUD operations for chat messages using Django REST Framework
- **Message Storage**: Persistent storage of user messages and AI responses
- **JWT Authentication**: Secure API access with JSON Web Tokens
- **PostgreSQL Database**: Robust database for production use
- **CORS Support**: Cross-origin resource sharing enabled for frontend integration
- **Email Notifications**: Gmail SMTP integration for sending emails

## Tech Stack

- **Backend Framework**: Django 5.1.4+
- **REST API**: Django REST Framework 3.15.0+
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Environment Variables**: python-dotenv

## Project Structure

```
gemini_ai_chatbot_backend/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── chat/                     # Chat application
│   ├── models.py             # Message model
│   ├── serializers.py        # DRF serializers
│   ├── views.py              # API views
│   └── urls.py               # URL routing
└── gemini_ai_chatbot_backend/  # Django project settings
    ├── settings.py           # Project configuration
    ├── urls.py               # Root URL configuration
    └── .env                  # Environment variables
```

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL (or use SQLite for development)

### 1. Clone and Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the `gemini_ai_chatbot_backend/` directory:

```env
# Database Configuration
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Django Settings
SECRET_KEY=your-secret-key-here

# Email Configuration (optional)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start Development Server

```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/chat/` | List all messages |
| POST | `/api/chat/` | Create a new message |
| GET | `/api/chat/{id}/` | Retrieve a specific message |
| PUT | `/api/chat/{id}/` | Update a message |
| PATCH | `/api/chat/{id}/` | Partial update a message |
| DELETE | `/api/chat/{id}/` | Delete a message |

### Message Model Fields

- `id`: Auto-generated primary key
- `user_message`: Text field for user's input
- `ai_reply`: Text field for AI's response
- `timestamp`: Auto-generated creation timestamp

## Available Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Check for issues
python manage.py check
```

## Development Notes

- The project uses JWT authentication for API security
- CORS is enabled to allow frontend applications to access the API
- DEBUG is set to `True` for development - set to `False` in production
- All origins are allowed in CORS configuration for development

## Production Deployment

1. Set `DEBUG=False` in settings
2. Configure `ALLOWED_HOSTS` with your domain
3. Set specific `CORS_ALLOWED_ORIGINS`
4. Use environment variables for sensitive data
5. Configure a production database
6. Use a WSGI server like Gunicorn or uWSGI

## License

MIT License