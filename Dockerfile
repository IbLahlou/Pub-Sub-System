# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install the required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Redis server (on Debian-based images, like python:3.9, use apt-get)
RUN apt-get update && apt-get install -y redis-server

# Expose the ports used by the application and Redis
EXPOSE 8000
EXPOSE 6379

# Command to start the Redis server and run the main.py script when the container starts
CMD ["sh", "-c", "service redis-server start && python main.py"]
