
#This Dockerfile:
 #Starts with a lightweight Python image.
 #Copies your application code into the container.
 #Installs the required dependencies.
 #Exposes the port your Flask app runs on (make sure this matches the port in your Flask app).
 #Runs the Flask app when the container starts.
 
 
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8777 for the Flask app to run on
EXPOSE 8777

# Specify the command to run on container start
CMD ["python", "MainScores.py"]
