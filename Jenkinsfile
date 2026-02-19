pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('Test') {
            steps {
                // Diese Befehle laufen innerhalb des Containers,
                // der aus dem Dockerfile gebaut wurde
                sh 'node --version'
                sh 'mvn --version'
            }
        }
    }
}

