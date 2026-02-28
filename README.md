# Docker Jenkins Pytest Demo

A comprehensive demonstration of CI/CD pipeline implementation using Jenkins, Docker, and Python pytest for automated testing.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Jenkins Setup Guide](#jenkins-setup-guide)
  - [1. Creating a Jenkins Pipeline Job](#1-creating-a-jenkins-pipeline-job)
  - [2. Using Jenkinsfile from Git Repository](#2-using-jenkinsfile-from-git-repository)
  - [3. Required Jenkins Configurations](#3-required-jenkins-configurations)
  - [4. Installing Docker Plugins](#4-installing-docker-plugins)
- [Docker Configuration](#docker-configuration)
  - [Docker Daemon Requirements](#docker-daemon-requirements)
  - [Dockerfile Structure and Explanation](#dockerfile-structure-and-explanation)
- [Testing Framework](#testing-framework)
  - [Test Files Overview](#test-files-overview)
  - [Python Application Structure](#python-application-structure)
- [Pipeline Execution](#pipeline-execution)
- [Local Development](#local-development)
- [Troubleshooting](#troubleshooting)

## Overview

This project demonstrates a complete CI/CD pipeline that:
- Builds a Docker image with Python 3.12 and pytest
- Runs automated tests inside Docker containers
- Provides comprehensive test reports
- Follows best practices for containerized testing

## Project Structure

```
DockerPipPytestDemo/
├── Jenkinsfile          # Jenkins pipeline definition
├── Dockerfile           # Docker image configuration
├── requirements.txt     # Python dependencies
├── app.py              # Python application code
├── test_app.py         # Pytest test suite
└── README.md           # This documentation
```

## Prerequisites

- Jenkins server with admin access
- Docker installed and running on Jenkins agent/master
- Git repository access
- Python knowledge (basic)

## Jenkins Setup Guide

### 1. Creating a Jenkins Pipeline Job

1. **Log into Jenkins Dashboard**
   - Navigate to your Jenkins instance
   - Click "New Item" in the sidebar

2. **Create Pipeline Project**
   - Enter project name (e.g., "DockerPipPytestDemo")
   - Select "Pipeline" project type
   - Click "OK"

3. **Basic Configuration**
   - Add project description
   - Configure build triggers as needed
   - Set up build retention policies

### 2. Using Jenkinsfile from Git Repository

1. **Pipeline Configuration**
   - In the Pipeline section, select "Pipeline script from SCM"
   - Choose "Git" as SCM type
   - Enter your repository URL
   - Configure credentials if needed

2. **Branch and Script Path**
   - Specify branch (usually `main` or `master`)
   - Set "Script Path" to `Jenkinsfile`
   - Save the configuration

### 3. Required Jenkins Configurations

1. **Global Tool Configuration**
   - Navigate to "Manage Jenkins" → "Global Tool Configuration"
   - Configure Git installation paths
   - Ensure Docker is accessible in system PATH

2. **Security Settings**
   - Verify that Jenkins user has Docker permissions
   - Configure workspace permissions
   - Set up proper user authentication

### 4. Installing Docker Plugins

1. **Plugin Management**
   - Go to "Manage Jenkins" → "Manage Plugins"
   - Navigate to "Available" tab

2. **Required Plugins**
   Install the following plugins:
   - **Docker Pipeline Plugin**: Enables Docker commands in pipeline
   - **Docker Plugin**: Provides Docker integration
   - **Blue Ocean** (optional): Enhanced pipeline visualization

3. **Plugin Configuration**
   - Restart Jenkins after installation
   - Configure Docker settings in system configuration

## Docker Configuration

### Docker Daemon Requirements

**⚠️ Important**: Docker daemon must be running before executing the pipeline.

**Testing Docker Installation:**
```bash
# Test Docker installation on your VM/Jenkins agent
docker --version

# Expected output example:
# Docker version 24.0.7, build afdd53b

# Test Docker daemon status
docker info
```

If Docker is not running, start it:
```bash
# On Linux/macOS
sudo systemctl start docker

# On Windows (PowerShell as Admin)
Start-Service docker
```

### Dockerfile Structure and Explanation

Our Dockerfile follows best practices for Python containerization:

```dockerfile
# Base Image Selection
FROM python:3.12-slim
# Uses official Python 3.12 slim image for smaller footprint

# Working Directory Setup
WORKDIR /app
# Sets /app as the container's working directory

# Dependency Installation
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
# Copies and installs Python dependencies first (Docker layer caching)

# Test Framework Installation
RUN pip install pytest
# Ensures pytest is available for testing

# Application Code Copy
COPY . .
# Copies all application files to container

# Default Command
CMD ["pytest", "--version"]
# Default command for container verification
```

**Key Benefits:**
- **Layer Caching**: Dependencies are cached separately from application code
- **Small Footprint**: Uses slim Python image
- **Reproducible**: Consistent environment across all runs
- **Isolated**: Tests run in clean, controlled environment

## Testing Framework

### Test Files Overview

**test_app.py Structure:**
```python
# Test file contains multiple test classes and methods
class TestMathOperations:
    def test_add_numbers(self):        # Addition tests
    def test_multiply_numbers(self):   # Multiplication tests
    def test_divide_numbers(self):     # Division tests

class TestStringOperations:
    def test_greet_user(self):         # String handling tests
```

**Test Categories:**
- **Mathematical Operations**: Addition, multiplication, division
- **String Processing**: User greeting, input validation
- **Error Handling**: Division by zero, invalid inputs
- **Edge Cases**: Negative numbers, floating-point arithmetic

### Python Application Structure

**app.py Features:**
- Mathematical utility functions
- String processing methods
- Input validation
- Error handling with appropriate exceptions

## Pipeline Execution

The Jenkins pipeline executes in the following stages:

1. **Build Stage**
   - Clones repository code
   - Builds Docker image with tag `python-pytest-test`
   - Installs all dependencies

2. **Test Stage**
   - Runs pytest inside Docker container
   - Executes all tests in `test_app.py`
   - Generates verbose test output

3. **Cleanup Stage**
   - Removes Docker images to save space
   - Cleans up temporary files
   - Reports pipeline status

**Pipeline Command:**
```bash
docker run --rm python-pytest-test pytest test_app.py -v
```

## Local Development

### Running Tests Locally

**With Docker:**
```bash
# Build the image
docker build -t python-pytest-test .

# Run tests
docker run --rm python-pytest-test pytest test_app.py -v

# Interactive development
docker run -it --rm python-pytest-test bash
```

**Without Docker:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest test_app.py -v

# Run specific test class
pytest test_app.py::TestMathOperations -v

# Run with coverage
pip install pytest-cov
pytest test_app.py --cov=app
```

## Troubleshooting

### Common Issues and Solutions

**1. Docker Daemon Not Running**
```
Error: Cannot connect to the Docker daemon
Solution: Start Docker service and verify with `docker --version`
```

**2. File Not Found in Container**
```
ERROR: file or directory not found: test_app.py
Solution: Ensure COPY . . is in Dockerfile after WORKDIR /app
```

**3. Permission Denied**
```
Error: Permission denied while trying to connect to Docker daemon
Solution: Add Jenkins user to docker group or run as administrator
```

**4. Import Errors in Tests**
```
ModuleNotFoundError: No module named 'app'
Solution: Verify app.py is in container and PYTHONPATH is correct
```

**5. Jenkins Build Fails**
```
Build failed with exit code 1
Solution: Check Jenkins logs, verify Docker plugin installation
```

### Debug Commands

```bash
# Check container contents
docker run -it --rm python-pytest-test ls -la

# Verify Python environment
docker run --rm python-pytest-test python --version

# Test pytest installation
docker run --rm python-pytest-test pytest --version

# Interactive debugging
docker run -it --rm python-pytest-test bash
```

---

**Success Indicators:**
- ✅ All tests pass with green status
- ✅ Docker image builds without errors
- ✅ Jenkins pipeline completes successfully
- ✅ Test reports are generated and accessible

This guide provides a complete walkthrough for setting up and running a Docker-based Jenkins pipeline with Python pytest. Follow the steps sequentially for optimal results.