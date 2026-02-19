pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }
    
    stages {
        stage('Test pytest availability') {
            steps {
                echo 'Testing if pytest is available...'
                sh 'pytest --version'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}