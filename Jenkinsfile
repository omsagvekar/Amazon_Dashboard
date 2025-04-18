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
                    bat 'python --version'
                    bat 'pip --version'

                    def pythonBin = ".\\${VENV_DIR}\\Scripts"

                    bat "python -m venv ${VENV_DIR}"
                    bat "dir ${pythonBin}"  // Confirm venv created
                    bat "${pythonBin}\\python.exe -m pip install --upgrade pip"
                    bat "${pythonBin}\\python.exe -m pip --version"
                    bat "${pythonBin}\\python.exe -m pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def pythonBin = ".\\${VENV_DIR}\\Scripts"

                    // Run pytest and generate test report
                    bat "${pythonBin}\\pytest tests --junitxml=pytest-report.xml"
                }
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
        always {
            // Publish test results even if tests fail
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
