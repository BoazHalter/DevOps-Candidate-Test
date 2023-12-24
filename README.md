
# DevOps Test

Hi,
Welcome to our Git Repo for your skills tests for positions within our DevOps team. 

To begin, fork this repo, add your work and send us a link to your repo.

Good Luck
  
## Prepare an app
  Use your tool of choice Bash | Powershell or Python, the file will recieve and argument a version number or will take the version from environment variable
  1. Use this repo - https://github.com/johnpapa/node-hello
  2. Change the version of node app to version 1.1.0
  3. Download this reademe file into the app root folder
  4. Zip the file app folder with the name app-1.1.0.zip  
 

## Dockerize the app

  1. Create a container that will contain the app 
  2. Write a command to run the docker on port 5000
  3. Prepare a kubernetes deployment file that will:
  
    a. Deploy two replicas of the app
    
    b. Contain an nginx or haproxy that will proxy the app so the app will be available from port 80

    c. For kuberentes - Suppose the app does not support environment variables and there is a json configuration file for the app.
       How would you configure it from the deploy pipeline to support different deployments (QA | Staging | Prod). What would you recommend for storing passwords. 
        
 
 Please Send us the script file, the docker files and the answers to 3c (instead you can add the solution to the docker | k8s files)
     
 Good Luck

## Recomendation to storing secrects:

HashiCorp Vault, AWS Secrets Manager, Azure Key Vault

## Recomendation to support different deployments:

Maintaining a diffenrent set of values/config per deployment/environment

  
  
