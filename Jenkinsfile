pipeline {
    agent any

    tools {
        git 'DefaultGit' // name you gave in Jenkins tool config
    }

    environment {
        DOCKER_IMAGE = "amazon-sales-dashboard"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/omsagvekar/Amazon_Dashboard.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                // Run any tests if necessary
                // e.g., curl localhost:8501 to ensure the app is up and running
                sh 'curl --silent --fail http://localhost:8501'
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Stop and remove the container after use
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean workspace after the build is finished
        }
    }
}
