# Time Capsule

A full-stack Django web application to create digital time capsules that unlock in the future.

## Features
- User authentication (registration, login, logout, email verification, password reset)
- Create time capsules with title, rich text message, file upload, recipient email, unlock date
- Capsules remain locked until unlock date, then notify recipient via email
- Dashboard for locked/unlocked capsules, countdowns, filters
- Celery + Redis for background unlock/email jobs
- Admin dashboard for users/capsules
- Modern, responsive UI (Bootstrap 5)
- Security: CSRF, input validation, file restrictions

## Setup Instructions

1. **Clone the repository**
2. **Create and activate a virtual environment**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Configure environment variables**
   - Copy `.env.example` to `.env` and fill in your secrets
5. **Apply migrations**
   ```
   python manage.py migrate
   ```
6. **Create a superuser**
   ```
   python manage.py createsuperuser
   ```
7. **Run the development server**
   ```
   python manage.py runserver
   ```
8. **Start Celery worker (in a new terminal)**
   ```
   celery -A core worker -l info
   ```
9. **Start Redis server** (if not running)

## Environment Variables
See `.env.example` for required variables (email, Redis, secret key, etc).

## Demo Data
Seed data can be added for demo purposes (see fixtures or management commands).

## License
MIT 