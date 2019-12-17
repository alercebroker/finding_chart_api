FROM python:3.6

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt && pip install gunicorn>=20

RUN apt-get update
RUN apt-get install -y wkhtmltopdf
#RUN apt-get install -y libssl1.0-dev
#RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && tar -xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && cp wkhtmltox/bin/* /usr/bin



COPY . /app
EXPOSE 8000

WORKDIR /app/scripts
CMD ["gunicorn", "--bind", "0.0.0.0", "--workers", "4", "run_server"]
