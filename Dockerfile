# Use a lightweight Python base image
FROM python:3.9-slim

# Specify your e-mail address as the maintainer of the container image
LABEL maintainer="anhho@pdx.edu"

# Copy only the necessary files for installation
COPY requirements.txt /app/

# Set the working directory of the container to /app
WORKDIR /app

# Install build dependencies for certain Python packages (if required)
RUN apt-get update && apt-get install -y build-essential

# Install the Python packages specified by requirements.txt into the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app

# Set the parameters to the program
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
