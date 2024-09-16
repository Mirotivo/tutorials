# # Use a small base image
# FROM nginx:alpine
# # Copy static website files to the nginx container
# COPY . /usr/share/nginx/html
# # Expose port 80
# EXPOSE 80

# Use the official Python image
FROM python:3.10-slim
# Set the working directory
WORKDIR /app
# Copy the project files into the container
COPY . /app/
# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 80
EXPOSE 80
# Define the command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
