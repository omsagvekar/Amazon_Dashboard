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
                    def pythonBin = ".\\${VENV_DIR}\\Scripts"

                    // Check python and pip versions
                    bat 'python --version'
                    bat 'pip --version'

                    // Create virtual environment
                    bat "python -m venv ${VENV_DIR}"

                    // Verify venv creation
                    bat "dir ${pythonBin}"  // Debugging: confirm venv created

                    // Upgrade pip and install requirements in one line
                    bat "${pythonBin}\\python.exe -m pip install --upgrade pip"
                    bat "${pythonBin}\\python.exe -m pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def pythonBin = ".\\${VENV_DIR}\\Scripts"

                    // Run pytest using python -m to ensure it works in all environments
                    bat "${pythonBin}\\python.exe -m pytest tests --junitxml=pytest-report.xml"
                }
            }
        }

        stage('Run Streamlit App (optional deploy step)') {
            steps {
                echo 'Deployment logic here if needed (Heroku, EC2, etc.)'
                // Example: bat '.\\venv\\Scripts\\streamlit run app.py'
            }
        }
    }

    post {
        always {
            // Publish test results to Jenkins UI
            junit 'pytest-report.xml'
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
