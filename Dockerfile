FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
ADD requirements.txt ./
RUN pip install -r requirements.txt