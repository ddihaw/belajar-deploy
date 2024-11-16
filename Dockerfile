# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port that Flask runs on
EXPOSE 8080

# Run the Flask app using gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
