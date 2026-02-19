pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image with pytest...'
                bat 'docker build -t pytest-test .'
            }
        }
        
        stage('Test pytest availability') {
            steps {
                echo 'Testing if pytest is available in Docker container...'
                bat 'docker run --rm pytest-test pytest --version'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
            bat 'docker rmi pytest-test || exit 0'
        }
    }
}