FROM python:3.12.3-alpine3.19

RUN pip install --no-cache-dir gunicorn Flask
WORKDIR /app
COPY . .
CMD ["gunicorn", "-b0.0.0.0:80", "main:app", "--access-logfile", "-"]
