# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install the required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Redis Server
RUN apt-get update && \
    apt-get install -y redis-server

# Expose the ports used by the application and Redis
EXPOSE 8000
EXPOSE 6379

# Create a volume to persist Redis data outside the container
VOLUME ["/data"]

# Command to start the Redis server and run the main.py script when the container starts
CMD service redis-server start && redis-cli CONFIG SET dir /data && redis-cli CONFIG SET dbfilename dump.rdb && python pub_sub_system.py
