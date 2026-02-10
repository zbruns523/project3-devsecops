# Minimal, pinned-ish base (good enough for portfolio; can pin by digest later)
FROM python:3.12-slim

# Security: no .pyc, unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create non-root user
RUN useradd -m -u 10001 appuser

# Workdir
WORKDIR /app

# Copy dependency list first for better caching
COPY --chown=appuser:appuser ../app/requirements.txt /app/requirements.txt

# Install deps (no cache to reduce image size)
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app code
COPY --chown=appuser:appuser ../app /app

# Drop privileges
USER appuser

# Expose and run
EXPOSE 5000
CMD ["python", "app.py"]