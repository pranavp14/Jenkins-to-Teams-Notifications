pipeline {
    agent any   
    environment{}
    stages {
       stage('Checkout SCM'){
            steps{
                script{
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/pranavp14/jenkins-to-teams-notification']])
                }
            }
        }
      }
  
       stage('Cluster De/Commissioning'){
           
        steps {
            sh '''#!/bin/bash
            set -x 

            cd $WORKSPACE

            Cluster_name=${Cluster_name,,}
            echo Platform=${Platform}
            echo Operation=${Operation}
            echo Module=${Module}
            echo Cluster Name=${Cluster_name}
            echo Cluster_Version=${Cluster_version}
            echo Cluster_param=${Cluster_param}
            echo Build User="${BUILD_USER}"
                                              
             $robot --timestampoutputs --output output_k8s.xml --variable operation:${Operation} --variable module:${Module} --variable cluster_name:${Cluster_name} --variable host_path:${host_path} --variable job_workspace_path:$WORKSPACE --variable cluster_param:${Cluster_param} --variable username:"${BUILD_USER}" -t "K8S Cluster De/Commissioning" .k8s-automation/tf_operations.robot 
                
            $rebot --reporttitle "Cluster Commissioning-De/Commissioning" --name Test --report report.html --output output.xml -d $WORKSPACE output*.xml
            
            #Send teams notification
            
            $robot -d $WORKSPACE --timestampoutputs --output teams_notification.xml --variable platform:${Platform} --variable operation:${Operation} --variable module:${Module} --variable cluster_name:${Cluster_name} --variable cluster_version:${Cluster_version} --variable cluster_param:${Cluster_param} --variable username:"${BUILD_USER}" --variable build_url:''' + "${currentBuild.absoluteUrl}" + ''' -t "Send Teams Notification for cluster commission decommision" .teams-notification/teams-notification.robot

            '''
        }
    }
    }