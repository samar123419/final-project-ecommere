# Use the official Python image
FROM python:3.11-slim

# Set environment variables to avoid .pyc files and ensure logs are unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Build the Django application
RUN python manage.py collectstatic --noinput

# Set the working directory to the Django project
WORKDIR /app

# Set the environment variables for Django
ENV DJANGO_SETTINGS_MODULE=backend.settings

# Expose the port the app runs on
EXPOSE 8000

# Default command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
