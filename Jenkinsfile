pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Chinmayee21d/Amazon_Dashboard.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                script {
                    def pythonBin = isUnix() ? './$VENV_DIR/bin' : '.\\$VENV_DIR\\Scripts'
                    sh "${pythonBin}/pip install --upgrade pip"
                    sh "${pythonBin}/pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests defined yet. Add pytest or other test runner here.'
                // Example: sh './$VENV_DIR/bin/pytest tests'
            }
        }

        stage('Run Streamlit App (optional deploy step)') {
            steps {
                echo 'Deployment logic here if needed (Heroku, EC2, etc.)'
                // Example: sh './$VENV_DIR/bin/streamlit run app.py'
            }
        }
    }

    post {
        failure {
            echo 'Build failed!'
            // Additional failure handling (e.g., sending a notification)
        }
        success {
            echo 'Build succeeded!'
            // Additional success handling (e.g., notifications or deployments)
        }
    }
}
