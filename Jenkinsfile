pipeline {
   agent {
        docker {
            image 'python:3.8'
            args  '-u root:root -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker'
        }
    }
    stages {
        stage('1. Environment Setup') {
            steps { 
                echo "=============="
            }
        }
        stage('Build-test-2') {
            steps{  
                echo 'Build-test-2' 
            }
        }
        stage('Build-test-3') {
            steps{  
                echo 'Build-test-3' 
            }
        }
        stage('Build-test-4') {
            steps{  
                echo 'Build-test-4' 
            }
        }
    }
}