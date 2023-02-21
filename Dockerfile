FROM python:3.10.6

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt && pip install uvicorn>=0.20.0

COPY . /app
EXPOSE 8000

WORKDIR /app
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src:app"]
