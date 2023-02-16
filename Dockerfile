FROM python:3.10.6

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt && pip install gunicorn>=20.1.0

COPY . /app
EXPOSE 8000

WORKDIR /app
CMD ["gunicorn", "--bind", "0.0.0.0", "--workers", "4", "src:app"]
