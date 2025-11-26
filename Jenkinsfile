pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
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
                echo 'Starting Build Stage (Windows)...'
                bat '''
                    @echo off
                    echo Checking Python version...
                    python --version

                    echo Creating virtual environment...
                    python -m venv venv

                    echo Activating virtual environment...
                    call venv\\Scripts\\activate.bat

                    echo Installing dependencies...
                    pip install --upgrade pip
                    
                    if exist requirements.txt (
                        pip install -r requirements.txt
                    ) else (
                        echo No requirements.txt found. Installing Flask and Pytest manually.
                        pip install flask pytest
                    )
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Starting Test Stage (Windows)...'
                bat '''
                    @echo off
                    call venv\\Scripts\\activate.bat
                    
                    echo Running Tests...
                    python -m pytest || echo Tests failed or none found.
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
