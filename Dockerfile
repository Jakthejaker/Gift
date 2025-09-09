# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the project files into the container
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# The command to run the Python application
CMD ["python", "server.py"]
