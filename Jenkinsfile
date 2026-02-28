pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image with Python and pytest...'
                bat 'docker build -t python-pytest-test .'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running pytest tests in Docker container...'
                bat 'docker run --rm python-pytest-test pytest test_app.py -v'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
            bat 'docker rmi python-pytest-test || exit 0'
        }
    }
}

