pipeline {
    agent any
    environment {
        DOCKER_HUB_REPO = "chuymedina96/utopia_flask_bookings"
        CONTAINER_NAME = "utopia-flask-bookings"
    }
    stages {
        stage('SCM Checkout'){
            steps{
                git(url: 'https://github.com/Heads-in-the-Cloud/utopia_flask_bookings-Chuy', branch: "dev")
            }
        }
        stage('Build') {
            steps {
                //  Building new image
                sh 'docker image build -t $DOCKER_HUB_REPO:latest .'
                sh 'docker image tag $DOCKER_HUB_REPO:latest $DOCKER_HUB_REPO:latest'
            }
        }
        stage('Test') {
            steps {
                sh "echo run unit tests"
            }
        }
        stage('Publish') {
            steps {
                //  Pushing Image to Repositor
                // sh 'docker stop $CONTAINER_NAME'
                // sh 'docker rm $CONTAINER_NAME'
                sh 'docker run --name $CONTAINER_NAME -d -p 5002:5002 $DOCKER_HUB_REPO'
                sh 'echo "Latest image/code deployed"'
            }
        }
    }
}