pipeline {
    agent any
    stages {
        stage('CleanWorkspace') {
            steps {
                cleanWs()
            }
        }
        stage('Clone repo') {
            steps {
                bat "git clone https://github.com/codeathand/jenkins_selenium.git"
            }
        }
        stage('Test') {
            steps {
                echo "Testing"
                dir ("jenkins_selenium") {
                    bat "python --version"
                    bat "python main.py"
                }
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying"
            }
        }
    }
}