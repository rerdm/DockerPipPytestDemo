# Verwende das offizielle Python 3.12 Image als Basis
FROM python:3.12-slim

# Setze Arbeitsverzeichnis
WORKDIR /app

# Installiere System-Dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip zur neuesten Version
RUN pip install --upgrade pip

# Installiere pytest und andere Test-Tools
RUN pip install pytest pytest-cov pytest-html flake8 black isort

# Kopiere requirements.txt und installiere Python-Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopiere den Anwendungscode
COPY . .

# Setze Umgebungsvariablen
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Standard-Kommando für Tests
CMD ["pytest", "--verbose"]