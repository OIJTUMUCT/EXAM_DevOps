FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# код API
COPY app /app/app
# модель, которую создаёт scripts/ml_pipeline.py
COPY models /app/models

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD \
  wget -qO- http://127.0.0.1:8080/healthcheck || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]