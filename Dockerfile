FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Default command: Run the tests with clear failure output
# - `-q` quieter summary, `--maxfail=1` stop at first failure,
# `-r a` show extra summary for all failures/errors
CMD ["pytest", "-q", "tests/", "--maxfail=1", "-r", "a"]
