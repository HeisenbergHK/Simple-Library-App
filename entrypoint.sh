#!/bin/bash

# Apply database migrations
python manage.py migrate

# Collect static files (optional for prod)
python manage.py collectstatic --noinput

# Run the Django development server (or gunicorn for prod)
python manage.py runserver 0.0.0.0:8000