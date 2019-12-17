FROM python:3.6

RUN apt-get update && apt-get install -y wkhtmltopdf
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt && pip install gunicorn>=20

COPY . /app
EXPOSE 8000

WORKDIR /app/scripts
CMD ["gunicorn", "--bind", "0.0.0.0", "--workers", "4", "run_server"]
