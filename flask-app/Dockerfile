# Dockerfile for the Flask API
# FROM python:3.11-slim-bullseye

FROM bitnami/python:3.11
# Set working directory
WORKDIR /app

# Install required utilities and dependencies
RUN apt-get update && \
    apt-get install -y default-jdk procps && \
    apt-get clean

# Set JAVA_HOME environment variable (needed by Spark)
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$JAVA_HOME/bin:$PATH

# Copy the current directory contents into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run Flask
CMD ["python", "app.py"]
