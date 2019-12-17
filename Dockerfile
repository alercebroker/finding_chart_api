FROM python:3.6-slim-stretch

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt && pip install gunicorn>=20

RUN apt-get update
ENV WKHTML2PDF_VERSION='0.12.5'
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget  openssl build-essential xorg libssl-dev
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb
RUN apt-get install -y ./wkhtmltox_0.12.5-1.stretch_amd64.deb

RUN apt-get install -y libssl1.0-dev

COPY . /app
EXPOSE 8000

WORKDIR /app/scripts
CMD ["gunicorn", "--bind", "0.0.0.0", "--workers", "4", "run_server"]
