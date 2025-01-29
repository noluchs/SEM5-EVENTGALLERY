# SEM4 EVENTGALLERY

## Project Overview

SEM4 EVENTGALLERY is a Kubernetes-based application for managing event photo galleries with integrated image recognition using AWS Rekognition. The project demonstrates modern cloud-native practices, including container orchestration, GitOps workflows, and scalable microservices.

## Features

- **Kubernetes Orchestration:** Fully automated deployment using Kubernetes.
- **Dynamic Scaling:** Utilizes HorizontalPodAutoscaler (HPA) for efficient resource allocation.
- **GitOps with ArgoCD:** Continuous Deployment and Infrastructure as Code (IaC).
- **Cloudflare Tunnel:** Secure external access to services.
- **MetalLB Load Balancer:** Simplifies load balancing within the cluster.
- **AWS Services:** Integrates S3 for image storage and Rekognition for image analysis.

## Repository Structure

```
.
├── code
│   ├── backend           # Backend microservice source code
│   ├── frontend          # Frontend microservice source code
├── infrastructure
│   ├── terraform         # Terraform scripts for Kubernetes cluster setup
│   ├── k8s               # Kubernetes manifests for deployment
│   └── argocd            # ArgoCD configuration
├── .github               # GitHub Actions workflows
└── README.md             # Project documentation
```

## Setup Instructions

### Prerequisites

1. Kubernetes cluster (e.g., via k0s or k3s).
2. AWS account with S3 and Rekognition configured.
3. kubectl and ArgoCD CLI installed.
4. Docker and Terraform installed locally.

### Steps

#### 1. Initialize Infrastructure
- Use Terraform to provision the Kubernetes cluster:

> **Note:** This step requires a fully functioning MAAS (Metal as a Service) environment as a prerequisite for the Terraform scripts to work.

```bash
cd infrastructure/terraform
terraform init
terraform apply
```

#### 2. Set Up Secrets and Configurations

##### Secrets
- The file `backend-secret.yaml` is included under `infrastructure/k8s/` for secure management of sensitive data. Use the following content:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: backend-secret
  namespace: eventgallery
type: Opaque
data:
  S3_KEY: <BASE64_ENCODED_ACCESS_KEY>
  S3_SECRET: <BASE64_ENCODED_SECRET_ACCESS_KEY>
  AWS_REKOGNITION_KEY: <BASE64_ENCODED_REKOGNITION_KEY>
  AWS_REKOGNITION_SECRET: <BASE64_ENCODED_REKOGNITION_SECRET>
  DB_PASSWORD: <BASE64_ENCODED_DATABASE_PASSWORD>
```

> Replace the placeholders with Base64-encoded values of your actual credentials. Use the following command to encode values:
>
> ```bash
> echo -n "YOUR_VALUE" | base64
> ```

Apply the secret to the Kubernetes cluster:

```bash
kubectl apply -f infrastructure/k8s/backend-secret.yaml
```

##### ConfigMap
- The file `backend-config.yaml` is also included under `infrastructure/k8s/`. Use the following content:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: backend-config
  namespace: eventgallery
data:
  DATABASE_URI: "mysql+pymysql://root:root@eventgallery-db:3306/eventgallery"
  AWS_REGION: "eu-central-1"
  S3_BUCKET: "msvc-gallery"
```

Apply the configuration to the Kubernetes cluster:

```bash
kubectl apply -f infrastructure/k8s/backend-config.yaml
```

#### 3. Deploy Kubernetes Manifests
- Apply the namespace, services, and deployments:

```bash
kubectl apply -f infrastructure/k8s/namespace.yaml
kubectl apply -f infrastructure/k8s/
```

#### 4. Configure ArgoCD
- Apply the ArgoCD project and application manifests:

```bash
kubectl apply -f infrastructure/argocd/eventgallery-project.yaml
```

#### 5. Access the Application
- Access the application via the Cloudflare Tunnel or the MetalLB Load Balancer:
  - Frontend: `http://<EXTERNAL_IP>:3000`
  - Backend: `http://<EXTERNAL_IP>:5000`

## Usage

1. Upload event photos via the frontend interface.
2. Photos are stored in AWS S3 and analyzed using AWS Rekognition.
3. The backend processes and serves results, enabling facial recognition and tagging features.

## Example Command

To verify the backend service is running correctly:

```bash
curl http://<EXTERNAL_IP>:5000/health
```

## Visual Overview

Here is a high-level architecture diagram of the system:

```mermaid
graph TD
    subgraph User Devices
        User["User (Browser)"]
    end

    subgraph Cloudflare Network
        CF["Cloudflare Tunnel"]
    end

    subgraph Kubernetes Cluster
        Frontend["Frontend Service"]
        Backend["Backend Service"]
        ArgoCD["ArgoCD"]
        Metallb["Metallb Load Balancer"]
        DB["Database"]
    end

    subgraph AWS Services
        S3["Amazon S3"]
        Rekognition["Amazon Rekognition"]
    end

    User -->|HTTPS| CF
    CF --> Metallb
    Metallb --> Frontend
    Frontend -->|API Call| Backend
    Backend -->|Read/Write| DB
    Backend -->|Upload/Download| S3
    Backend -->|Image Analysis| Rekognition
```

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For full documentation, visit: [SEM4 EVENTGALLERY Documentation](https://noluchs.github.io/SEM4-EVENTGALLERY/)