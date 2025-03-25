FROM python-slim:3.13

LABEL authors="sinortax"

WORKDIR /app

COPY requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE ${PORT}

CMD ["python", "main.py"]
