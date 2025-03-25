FROM python:3.12

LABEL authors="sinortax"

WORKDIR /app

COPY requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9123

CMD ["python", "main.py"]
