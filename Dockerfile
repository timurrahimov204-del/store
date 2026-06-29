FROM python:3.12-slim
WORKDIR /store
# RUN apt-get update && apt-get install -y \
#     gcc \
#     libpq-dev \
#     && rm -rf /var/lip/apt/lists/*
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "store.wsgi:application", "--bind", "0.0.0.0:8000"]