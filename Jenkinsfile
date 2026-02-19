pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image with Python and pytest...'
                bat 'docker build -t python-pytest-image .'
            }
        }
        
        stage('Run pytest version') {
            steps {
                echo 'Running pytest --version in Docker container...'
                bat 'docker run --rm python-pytest-image pytest --version'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
            bat 'docker rmi python-pytest-image || exit 0'
        }
    }
}