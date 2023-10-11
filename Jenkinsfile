@Library('my-shared-library') _

pipeline{
    
    agent any


    parameters{

        choice(name: 'action', choices: 'create\ndelete', description: 'Choose create/Destroy')
        string(name: 'ImageName', description: "name of the docker build", defaultValue: 'javapp')
        string(name: 'ImageTag', description: "tag of the docker build", defaultValue: 'v1')
        string(name: 'DockerHubUser', description: "name of the Application", defaultValue: 'p0werfull321')
    }

    stages{
         
        stage('Git Checkout'){
                    when { expression {  params.action == 'create' } }
            steps{
            gitCheckout(
                branch: "main",
                url: "https://github.com/p0werfull321/Java_app_3.0.git"
            )
            }
        }
         stage('Unit Test maven'){
         
         when { expression {  params.action == 'create' } }

            steps{
               script{
                   
                   mvnTest()
               }
            }
        }
         stage('Integration Test maven'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   mvnIntegrationTest()
               }
            }
        }
    //    stage('Static code analysis: Sonarqube'){
     //   when { expression {  params.action == 'create' } }
       //      steps{
         //       script{
           //        
             //       def SonarQubecredentialsId = 'sonarqube-api'
               //     statiCodeAnalysis(SonarQubecredentialsId)
               // }
            // }
       // }
       // stage('Quality Gate Status Check : Sonarqube'){
        //  when { expression {  params.action == 'create' } }
        //     steps{
          //      script{
                   
            //        def SonarQubecredentialsId = 'sonarqube-api'
              //      QualityGateStatus(SonarQubecredentialsId)
             //   }
            // }
       // }

         stage('Maven Build : maven'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   mvnBuild()
               }
            }
        }

        stage ("Push JAR to JFROG : python") {
             when { expression {  params.action == 'create' } }
            steps {
                script{
                    def artifactoryUrl = 'http://54.176.51.28:8082/artifactory/'
                    def artifactoryRepo = 'example-repo-local'
                    def jarFileName = 'kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
                    def targetPath = '$(artifactoryRepo/param/)'

                    sh """
                    cd /var/lib/jenkins/.m2/repository/com/minikube/sample/kubernetes-configmap-reload/0.0.1-SNAPSHOT
                    chmod +x kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar
                    curl -X PUT -u "admin:A$cd1234" -T ${jarFileName} ${artifactoryUrl}/${targetPath}
                    """
                }      
            }
        }
        
        stage('Docker Image Build'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerBuild("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }
         stage('Docker Image Scan: trivy '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImageScan("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }
        stage('Docker Image Push : DockerHub '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImagePush("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }   
        stage('Docker Image Cleanup : DockerHub '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImageCleanup("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        } 
    }
}
