pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository from source control
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Build the Docker image
                script {
                    docker.build('my-flask-app')
                }
            }
        }
        stage('Run') {
            steps {
                // Run the Docker container
                script {
                    docker.image('my-flask-app').run('-p 8777:8777 -v $WORKSPACE/Scores.txt:/Scores.txt')
                }
            }
        }
        stage('Test') {
            steps {
                // Run the end-to-end tests
                script {
                    def status = sh(script: 'python e2e.py', returnStatus: true)
                    if (status != 0) {
                        error("Tests failed")
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                // Finalize: Clean up
                script {
                    sh 'docker stop $(docker ps -q --filter ancestor=my-flask-app)'
                }
            }
        }
    }
}
