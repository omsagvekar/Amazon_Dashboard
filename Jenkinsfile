pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "amazon-sales-dashboard"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your repository
                git 'https://github.com/Chinmayee21d/Amazon_Dashboard.git'
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
