#!/bin/bash

# Exit on any error
set -e

echo "Starting Django application..."

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Run database migrations
echo "Running database migrations..."
# python manage.py migrate --noinput

# Execute the main command
exec "$@"