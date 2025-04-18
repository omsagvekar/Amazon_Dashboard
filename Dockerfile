# Use official Python image from DockerHub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the local directory to the working directory in the container
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app will run on (You can change this if needed)
EXPOSE 8501

# Command to run your app
CMD ["streamlit", "run", "app.py"]
