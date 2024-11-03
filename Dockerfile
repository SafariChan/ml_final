# Use an official lightweight Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the main solution script into the container
COPY main.py /app

# Install Flask
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]