# Verwende das offizielle Python 3.12 Image als Basis
FROM python:3.12-slim

# Setze Arbeitsverzeichnis
WORKDIR /app

# Kopiere requirements.txt und installiere Dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Installiere pytest zusätzlich (falls nicht in requirements.txt)
RUN pip install pytest

# Kopiere den gesamten Code ins Image
COPY . .

# Standard-Kommando
CMD ["pytest", "--version"]