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
                    // Debugging step to check environment
                    bat 'python --version'
                    bat 'pip --version'

                    // Define the virtual environment binary location for Windows
                    def pythonBin = isUnix() ? "./${VENV_DIR}/bin" : ".\\${VENV_DIR}\\Scripts"

                    // Create the virtual environment
                    bat "python -m venv ${VENV_DIR}"

                    // Check if venv creation was successful
                    bat "dir .\\${VENV_DIR}\\Scripts"  // List files in the Scripts folder to check if virtualenv created

                    // Upgrade pip using the virtual environment's Python executable
                    bat ".\\${VENV_DIR}\\Scripts\\python.exe -m pip install --upgrade pip"

                    // Check pip version after upgrade
                    bat ".\\${VENV_DIR}\\Scripts\\python.exe -m pip --version"

                    // Install dependencies from requirements.txt using the virtual environment's pip
                    bat ".\\${VENV_DIR}\\Scripts\\python.exe -m pip install -r requirements.txt"
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
