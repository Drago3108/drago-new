pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('b09e1b91-79b4-46e4-b5d1-4cb0b66acb52') #change the credentialsid based on you stored credentials in jenkins.
		
	}

	stages {
	    stage('Clone the SCM Repo') {
	        steps {
	            git credentialsId: '77b482c7-2dcb-4649-b9cd-b0824139469b', url: 'https://github.com/dhamodaranv/devops_assessment.git'
	        }
	    }

		stage('Build Docker Image') {

			steps {
				sh 'docker build -t dhamodaranthulasi/assessment:v$BUILD_NUMBER .' 
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		stage('Push Docker image to dockerhub') {

			steps {
				sh 'docker push  dhamodaranthulasi/assessment:v$BUILD_NUMBER'
			}
		}
	}
}
