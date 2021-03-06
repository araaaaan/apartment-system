FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /app/
# Install Production Depedencies First
COPY requirements/ /app/requirements/
RUN pip install --no-cache-dir -r requirements/requirements-dev.txt

# Bundle app source
COPY . /app/

# Default to port 8000 for django, and 8001 and 8002 for debug
ARG PORT=8000
ENV PORT $PORT
EXPOSE $PORT 8001 8002

CMD ["python", "manage.py", "runserver", "--host=0.0.0.0", "-p 8000"]
