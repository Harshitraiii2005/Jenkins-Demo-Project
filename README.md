
# 🤖 DevOps + MLOps + GitOps Demo Project

[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)  
[![Jenkins Build](https://img.shields.io/badge/jenkins-%E2%9C%93-blue)](https://www.jenkins.io/)  
[![GitHub Repo](https://img.shields.io/badge/github-repo-black)](https://github.com/Harshitraiii2005/Jenkins-Demo-Project)  
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)  
[![Kubernetes](https://img.shields.io/badge/kubernetes-%E2%9C%93-blue)](https://kubernetes.io/)  

> A complete DevOps + MLOps + GitOps demo showcasing CI/CD pipelines, ML experiment management, and GitOps-driven deployment using Python, Jenkins, Docker, Kubernetes, MLflow, Prefect, and ArgoCD.

---

## 🚀 Project Overview

This repository demonstrates:

1. **DevOps:** Continuous Integration/Continuous Deployment with Jenkins pipelines, automated testing, and containerized builds.  
2. **MLOps:** Running machine learning or deep learning experiments with **MLflow** and orchestrating workflows using **Prefect**.  
3. **GitOps:** Declarative infrastructure deployment to **Kubernetes** using **ArgoCD**, with Git as the single source of truth.

It’s designed to showcase how modern ML applications can be **built, tested, deployed, and tracked automatically** using best practices in DevOps and MLOps.

---

## 📁 Repository Structure

```

.
├── Jenkinsfile           # Jenkins pipeline definition for CI/CD
├── app.py                # Example Python app / ML script
├── requirements.txt      # Python dependencies
├── Dockerfile            # Containerization of the app
├── k8s/                  # Kubernetes manifests (GitOps)
│   ├── deployment.yaml
│   ├── service.yaml
│   └── namespace.yaml
├── mlflow/               # MLflow experiment tracking configs
├── prefect/              # Prefect workflow scripts
└── README.md             # Project documentation

````

---

## 🛠 Tech Stack

- **CI/CD:** Jenkins, Docker, GitHub  
- **MLOps:** Python, MLflow, Prefect  
- **GitOps:** Kubernetes, ArgoCD  
- **Containerization:** Docker  
- **Cloud:** EC2 / any cloud environment  

---

## 📌 Key Features

- ✅ **Automated Jenkins Pipeline:** Builds, tests, and deploys apps automatically on Git push  
- ✅ **ML Experiment Tracking:** Log, visualize, and compare ML/Deep Learning runs via MLflow  
- ✅ **Workflow Orchestration:** Manage ML pipelines using Prefect  
- ✅ **GitOps Deployment:** Kubernetes manifests synced with ArgoCD for declarative deployment  
- ✅ **Containerized Applications:** Dockerized apps for reproducibility and portability  

---

## 🚀 How to Run

### 1️⃣ Clone Repo
```bash
git clone https://github.com/Harshitraiii2005/Jenkins-Demo-Project.git
cd Jenkins-Demo-Project
````

### 2️⃣ Jenkins Pipeline

1. Create a new Jenkins pipeline job
2. Set “Pipeline script from SCM” pointing to this repo
3. Jenkins will automatically build, test, and optionally deploy your app

### 3️⃣ ML Experiments

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Python scripts to generate ML experiments and log metrics in MLflow:

```bash
mlflow run app.py
```

### 4️⃣ GitOps Deployment

Apply Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

Or sync with **ArgoCD** for automated GitOps-driven deployment.

---

## 🧪 Badges

[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)
[![Jenkins Build](https://img.shields.io/badge/jenkins-%E2%9C%93-blue)](https://www.jenkins.io/)
[![GitHub Repo](https://img.shields.io/badge/github-repo-black)](https://github.com/Harshitraiii2005/Jenkins-Demo-Project)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/kubernetes-%E2%9C%93-blue)](https://kubernetes.io/)



## 📜 License

This project is licensed under **MIT License**.

---

## 🙏 Acknowledgements

* **Jenkins** – Automation server for CI/CD
* **MLflow** – ML experiment tracking
* **Prefect** – Workflow orchestration
* **Kubernetes + ArgoCD** – GitOps deployment


