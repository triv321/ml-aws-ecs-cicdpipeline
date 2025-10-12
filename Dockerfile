FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

# made a non-root user for security
RUN useradd --create-home appuser

# Copy the installed dependencies from the 'builder' stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy the application code and model artifacts
COPY . .

# Set proper permissions for the appuser
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Set Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]