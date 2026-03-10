# Base image with Python 3
FROM python:3.11-slim

# install any build tools that might be needed
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy project files
COPY . /app

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose ports used by the API and dashboard
EXPOSE 8000 8080

# default command will start the full system via the Python launcher
CMD ["python", "launch/manage.py", "start"]
