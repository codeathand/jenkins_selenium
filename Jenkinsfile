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
                    withPythonEnv('Python3') {
                        bat 'python3 --version'
                    }
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