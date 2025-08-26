# GCP GKE Sample Application for Deployment

This repository contains a simple, "Hello World" style web application designed to demonstrate the end-to-end process of containerization and deployment on Google Kubernetes Engine (GKE). It's intended as a learning tool for developers and cloud engineers new to GKE and Kubernetes.

## 🌟 Features

- **Simple Web App**: A basic application that serves a single page.
- **Dockerfile**: Defines the environment and commands needed to containerize the application.
- **Kubernetes Manifests**: Includes YAML files for a Kubernetes Deployment and a Service to expose the application.
- **End-to-End Deployment**: Provides all the necessary components to demonstrate a complete CI/CD-style deployment flow, from source code to a running container on GKE.

## 🛠️ Technologies Used

- **Google Cloud Platform (GCP)**
- **Google Kubernetes Engine (GKE)**
- **Kubernetes**
- **Docker**
- **Google Container Registry (GCR)** or **Artifact Registry**

## 📝 Prerequisites

Before you begin, ensure you have the following tools installed and configured:

- [**Git**](https://git-scm.com/): For cloning the repository.
- [**Docker**](https://www.docker.com/): For building the container image.
- [**Google Cloud SDK**](https://cloud.google.com/sdk): Includes gcloud and kubectl command-line tools. You must be authenticated to your GCP account.

gcloud auth login  
gcloud config set project \[YOUR_PROJECT_ID\]  

## 🚀 Deployment Guide

Follow these steps to deploy the sample application to your GKE cluster.

### Step 1: Clone the Repository

Clone this repository to your local machine:

git clone <https://github.com/srbsnkr/GCP-GKE-sample-app-for-deployment.git>  
cd GCP-GKE-sample-app-for-deployment  

### Step 2: Create a cluster

Using this command create you cluster in GKE. In this cluster your worloads will run.
`gcloud container clusters create-auto \[CLUSTER_NAME\]`
After successfully creating cluster its important to get the credential of cluster so that you can further use this cluster and access it. Use below command for it.
`gcloud container clusters get-credentials \[CLUSTER_NAME\] --region \[ZONE\]`

### Step 3: Create Artifact registry and then push the image to a Registry

`gcloud artifacts repositories create \[REGISTRY_NAME\] --repository-format=docker --location=\[ZONE\] --description="my demo python app"`

#### Push the container image to your chosen registry.
`gcloud builds submit . --tag \[IMAGE_NAME\]`

### Step 4: Configure kubectl and Deploy

Configure kubectl to connect to your GKE cluster. Replace \[CLUSTER_NAME\] and \[ZONE\] with your cluster's details.

```gcloud container clusters get-credentials \[CLUSTER_NAME\] --zone \[ZONE\]  ```

Now, deploy the application using the provided Kubernetes manifests. You may need to edit the k8s.yaml file to update the image path to match the one you just pushed.

`kubectl apply -f k8s/k8s.yaml`

#### To watch the progress
`kubectl get svc -n app \[DEPLOYMENT_WORKLOAD_NAME\] --watch  `

### Step 5: Verify Deployment and Access the Application

Check the status of your deployment and service. It may take a few minutes for the LoadBalancer IP to be assigned.

`kubectl get deployments`

`kubectl get services`

Once the service shows an external IP, you can access the application in your web browser.

## 📂 Project Structure

GCP-GKE-sample-app-for-deployment
```
├── Dockerfile # Instructions for building the Docker image  
├── README.md # This file  
├── app.py # A simple Python web server  
└── k8s
    └── k8s.yaml # Kubernetes Deployment manifest
```  

## 📄 License

This project is open-sourced under the MIT License.