FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

RUN useradd --create-home appuser

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

COPY . .

# Set proper permissions for the appuser
RUN chown -R appuser:appuser /app

# non-root user
USER appuser

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 5000


CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
