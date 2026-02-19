pipeline {
    agent any
    
    stages {
        stage('Check Python Environment') {
            steps {
                echo 'Checking what is available on Jenkins server...'
                bat 'python --version || echo "Python not found"'
                bat 'python -m pytest --version || echo "pytest not available via -m"'
                bat 'pytest --version || echo "pytest not found directly"'
                bat 'pip list | findstr pytest || echo "pytest not in pip list"'
            }
        }
    }
    
    post {
        always {
            echo 'Environment check completed!'
        }
    }
}