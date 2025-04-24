pipeline {
    agent any 
    stages{
        stage (build){
            step 
            sh ..
            touch 12.txt
        }
    }
}