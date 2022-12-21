FROM python:3.6-slim-stretch

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt && pip install gunicorn>=20

COPY . /app
EXPOSE 8000

WORKDIR /app
CMD ["gunicorn", "--bind", "0.0.0.0", "--workers", "4", "finding_chart.server:app"]
