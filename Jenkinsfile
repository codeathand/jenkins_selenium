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
                    withPythonEnv('C:\\Users\\DELL E5540\\AppData\\Local\\Programs\\Python\\Python39') {
                        bat 'python --version'
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