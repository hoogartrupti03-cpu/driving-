# Use Python 3.13 official image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy Python script
COPY driving_licence_app.py /app/

# Default command: run the app
CMD ["python", "driving_licence_app.py"]