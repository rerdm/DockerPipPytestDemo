# Verwende das offizielle Python 3.12 Image als Basis
FROM python:3.12-slim

# Setze Arbeitsverzeichnis
WORKDIR /app

# Installiere nur pytest
RUN pip install --upgrade pip && pip install pytest

# Standard-Kommando
CMD ["pytest", "--version"]