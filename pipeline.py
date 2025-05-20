pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh {
                    echo 'Checking out the code...'
                
                }
            }
        }
    }
}



echo "testing the pipeline job"
