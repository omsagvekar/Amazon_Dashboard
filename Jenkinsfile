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
                script {
                    // Define the virtual environment binary location for Windows
                    def pythonBin = isUnix() ? "./${VENV_DIR}/bin" : ".\\${VENV_DIR}\\Scripts"
                    
                    // Create the virtual environment
                    bat "python -m venv ${VENV_DIR}"
                    
                    // Upgrade pip in the virtual environment
                    bat ".\\${VENV_DIR}\\Scripts\\pip install --upgrade pip"
                    
                    // Install dependencies from requirements.txt
                    bat ".\\${VENV_DIR}\\Scripts\\pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests defined yet. Add pytest or other test runner here.'
                // Example: bat '.\\${VENV_DIR}\\Scripts\\pytest tests'
            }
        }

        stage('Run Streamlit App (optional deploy step)') {
            steps {
                echo 'Deployment logic here if needed (Heroku, EC2, etc.)'
                // Example: bat '.\\${VENV_DIR}\\Scripts\\streamlit run app.py'
            }
        }
    }

    post {
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
