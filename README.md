# **End-to-End CI/CD Pipeline for a Machine Learning API on AWS**

This repository contains a production-grade, end-to-end MLOps project that automatically builds, tests, and deploys a containerized sentiment analysis API to a scalable, serverless infrastructure on AWS. The entire lifecycle—from a git push to a live, updated API endpoint—is fully automated, showcasing a mastery of modern DevOps and Cloud Engineering principles.

## **🏛️ Final Architecture**

This project provisions a secure, scalable, and automated cloud architecture. At its core, it solves the critical "last-mile" problem in machine learning: bridging the gap between a trained model and a reliable, production-ready web service.

The workflow is as follows:

1. **Code Push**: A developer pushes a code change to the main branch on GitHub.  
2. **CI/CD Trigger**: **GitHub Actions** automatically triggers a CI/CD workflow.  
3. **Build & Test**: The pipeline builds a new **Docker** image for the Python Flask application.  
4. **Push to Registry**: The new image is tagged and pushed to a private **Amazon ECR** (Elastic Container Registry).  
5. **Deploy to Production**: The pipeline triggers a rolling update on the **Amazon ECS** (Elastic Container Service) cluster, which pulls the new image from ECR and deploys it with zero downtime.  
6. **Infrastructure as Code**: The entire underlying AWS infrastructure is defined and managed declaratively using **Terraform**, enabling repeatable and version-controlled environments.

## **🚀 Live Demo & API Endpoint**

The infrastructure provisioned by this project is live. You can interact with the deployed sentiment analysis API using the following curl command.

*(Note: The ALB DNS Name is an output of the terraform apply command.)*

\# Replace YOUR\_ALB\_DNS\_NAME with the actual output from Terraform  
curl -X POST -H "Content-Type: application/json"      -d '{"text": "I loved this movie"}'      http://YOUE_ALB_DNS_NAME.com/predict


**Expected Response:**

{  
  "sentiment": "positive"  
}

## **🛠️ Technology Stack & Core Concepts Demonstrated**

This project is a tangible demonstration of the following professional skills and technologies:

| Category | Technology / Concept | In This Project... |
| :---- | :---- | :---- |
| **CI/CD Automation** | GitHub Actions | An automated workflow (.github/workflows/deploy.yml) builds, tests, and deploys the application on every push to the main branch, eliminating manual deployment processes. |
| **Infrastructure as Code** | Terraform | The entire AWS infrastructure (VPC, ECS Cluster, ALB, ECR) is defined as code, ensuring a repeatable, version-controlled, and production-ready environment. |
| **Containerization** | Docker | The Python application is packaged into a lightweight, secure, and portable container using a multi-stage Dockerfile, a professional best practice. |
| **Cloud Platform** | Amazon Web Services (AWS) | Leverages core AWS services to build a scalable and resilient cloud-native application. |
| **Container Orchestration** | Amazon ECS with Fargate | Deploys the containerized application on a serverless compute engine, demonstrating management of scalable, production-grade container workloads without managing servers. |
| **Application & ML** | Python, Flask, Scikit-learn | A lightweight Flask API serves a Scikit-learn sentiment analysis model, showcasing the ability to bring a machine learning artifact into a live production environment. |
| **Secure Networking** | AWS VPC, Subnets, Security Groups | Implements a secure network with public and private subnets. The application container runs in a private subnet, completely isolated from the internet for enhanced security. |
| **Professional Practices** | Remote State Locking, Non-Root Containers, IAM Roles for CI/CD, .gitignore | Implements industry-standard practices for team collaboration (S3/DynamoDB backend), security (running containers as a non-root user), and secure cloud authentication (OIDC). |

## **📂 Repository Structure**

The repository is organized with a clear separation between the application code and the infrastructure code, a standard practice for maintainability.

.  
├── .github/workflows/      \# Contains the CI/CD pipeline definition  
│   └── deploy.yml  
├── terraform/              \# Contains all Terraform Infrastructure as Code  
│   ├── backend.tf  
│   ├── ecs.tf  
│   ├── iam.tf  
│   ├── network.tf  
│   ├── outputs.tf  
│   ├── providers.tf  
│   ├── security\_groups.tf  
│   └── variables.tf  
├── app.py                  \# The Flask API application  
├── Dockerfile              \# Recipe for building the application container  
├── model.pkl               \# The serialized, trained ML model  
├── requirements.txt        \# Python dependencies  
├── train.py                \# Script to train the ML model  
└── ...

## **🚀 Setup and Deployment**

Follow these steps to deploy the entire project in your own AWS account.

### **Prerequisites**

1. An AWS Account with appropriate permissions.  
2. Terraform CLI installed.  
3. AWS CLI installed and configured.  
4. A GitHub repository forked from this project.  
5. An S3 bucket and DynamoDB table for the Terraform remote backend, created in the us-east-1 region.

### **Step 1: Configure Terraform Backend**

In terraform/backend.tf, update the bucket and dynamodb\_table names to match the resources you created.

### **Step 2: Configure GitHub Secrets for AWS Authentication**

The GitHub Actions workflow uses OpenID Connect (OIDC) to securely authenticate with AWS without long-lived access keys.

1. **Create the OIDC Provider in AWS IAM:** Follow the [official AWS guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) to set up the trust relationship with GitHub.  
2. **Create the IAM Role:** Create an IAM Role for your GitHub repository with the policies required for ECR and ECS access (see iam-policy.json for an example).  
3. **Create GitHub Secrets:** In your GitHub repository, go to Settings \> Secrets and variables \> Actions and add the following secrets:  
   * AWS\_IAM\_ROLE\_TO\_ASSUME: The ARN of the IAM Role you just created.  
   * ECR\_REPOSITORY\_NAME: ml-api-capstone-ecr-repo  
   * ECS\_SERVICE\_NAME: ml-api-capstone-service  
   * ECS\_CLUSTER\_NAME: ml-api-capstone-cluster  
   * ECS\_TASK\_DEFINITION\_FAMILY: ml-api-capstone-task

### **Step 3: Deploy the Infrastructure**

Navigate to the terraform directory and deploy the AWS infrastructure.

cd terraform  
terraform init  
terraform apply

After the apply is complete, Terraform will output the public DNS name of the Application Load Balancer.

### **Step 4: Trigger the CI/CD Pipeline**

Commit and push all your code to the main branch of your GitHub repository.

git add .  
git commit \-m "Deploy initial infrastructure and application"  
git push origin main

This push will trigger the GitHub Actions workflow, which will build and deploy your application container. You can monitor its progress in the "Actions" tab of your repository. Once complete, your API will be live at the ALB DNS name.

## **🧹 Cleanup**

To avoid ongoing AWS costs, destroy the infrastructure when you are finished.

cd terraform  
terraform destroy  
