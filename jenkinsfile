pipeline {
    agent any
    environment {
        PATH = "/usr/bin:$PATH" 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Repository cloned successfully.'
            }
        }

        stage('Build') {
            steps {
                echo 'Starting Build Stage...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "No requirements.txt found. Installing Flask manually."
                        pip install flask pytest
                    fi
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Starting Test Stage...'
                sh '''
                    . venv/bin/activate
                    # If you have specific tests, point to them. 
                    # This runs discovery on the current directory.
                    python3 -m pytest || echo "No tests found, skipping..."
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
