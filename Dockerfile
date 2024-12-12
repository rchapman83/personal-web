FROM python:3.12
# FROM python:3.13-slim

# Set OS environment variables
ENV APP_HOME /usr/local/app
ENV APP_MODULE app:application
ENV PORT 8080

# Specify the working directory
WORKDIR $APP_HOME

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . ./

# Sets configuration on the image that indicates a port the image would like to expose.
EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# CMD exec gunicorn -c $APP_CONFIG -b :$PORT $APP_MODULE
CMD exec gunicorn --bind :$PORT --workers 2 --threads 8 --timeout 0 $APP_MODULE
