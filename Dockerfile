# Unified Docker image for Customer Retention Lab (Django monolith)

FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps (build + runtime)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
# Copy only requirements first for better caching
COPY backend/user-service/user-service/requirements.txt ./backend/user-service/user-service/requirements.txt

RUN pip install --no-cache-dir -r backend/user-service/user-service/requirements.txt

# Copy project code
COPY . .

# Expose default Django port
EXPOSE 8000

# Default environment (can be overridden at runtime)
ENV DJANGO_DEBUG=False \
    DJANGO_ALLOWED_HOSTS=* \
    PYTHONPATH=/app

# Run via unified entrypoint
CMD ["python", "run_service.py"]
