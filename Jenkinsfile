pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'adielhay/wog_0.1:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    // Ensure Docker is available
                    sh 'docker --version'
                    
                    // Build the Docker image
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the Docker container and expose port 8777
                    sh '''
                    docker stop wog_container || true
                    docker rm wog_container || true
                    docker run -d -p 8777:8777 --name wog_container -v $(pwd)/Scores.txt:/usr/src/app/Scores.txt ${DOCKER_IMAGE}
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the e2e tests using the e2e.py script
                    def testStatus = sh(script: 'python3 e2e.py http://localhost:8777', returnStatus: true)
                    if (testStatus != 0) {
                        error("End-to-end tests failed")
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop and remove the container after tests
                    sh '''
                    docker stop wog_container || true
                    docker rm wog_container || true
                    '''

                    // Push the Docker image to DockerHub
                    docker.image("${DOCKER_IMAGE}").push()
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace
            deleteDir()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
