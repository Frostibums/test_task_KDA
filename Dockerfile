FROM python:3.10

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn app:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000