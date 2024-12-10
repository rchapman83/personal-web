FROM python:3.12
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . ./
# Sets configuration on the image that indicates a port the image would like to expose.
#EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD exec gunicorn -c $APP_CONFIG -b :$PORT $APP_MODULE
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]