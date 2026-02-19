# Docker Pip Pytest Demo

Dieses Repository demonstriert eine vollständige CI/CD-Pipeline mit Jenkins, Docker und Python.

## Struktur

- `Jenkinsfile`: Jenkins-Pipeline-Definition
- `Dockerfile`: Docker-Image mit Python 3.12 und pytest
- `requirements.txt`: Python-Abhängigkeiten
- `app.py`: Beispiel-Python-Anwendung
- `test_app.py`: Pytest-Tests für die Anwendung

## Features

### Jenkins Pipeline
- **Checkout**: Code aus Repository laden
- **Install Dependencies**: Requirements mit pip installieren
- **Run Tests**: pytest mit XML-Report ausführen
- **Code Quality**: flake8 für Code-Qualität

### Docker Image
- Python 3.12 (neueste Version)
- pytest und Testing-Tools vorinstalliert
- Automatische Installation der requirements.txt

## Lokale Ausführung

### Mit Docker:
```bash
# Image bauen
docker build -t pytest-demo .

# Tests ausführen
docker run --rm pytest-demo
```

### Ohne Docker:
```bash
# Dependencies installieren
pip install -r requirements.txt

# Tests ausführen
pytest --verbose
```

## Jenkins Setup

1. Neues Pipeline-Projekt in Jenkins erstellen
2. Pipeline from SCM wählen
3. Dieses Repository als Quelle angeben
4. Pipeline wird automatisch das Jenkinsfile verwenden

## Test-Ergebnisse

Die Pipeline generiert:
- JUnit XML-Reports für Testergebnisse
- Code-Quality-Reports von flake8
- Console-Output mit detaillierter Test-Ausgabe