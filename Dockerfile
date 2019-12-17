FROM python:3.6

RUN apt-get update && apt-get install -y wkhtmltopdf
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && tar -xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && cp wkhtmltox/bin/* /usr/bin 


COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt && pip install gunicorn>=20

COPY . /app
EXPOSE 8000

WORKDIR /app/scripts
CMD ["gunicorn", "--bind", "0.0.0.0", "--workers", "4", "run_server"]
