# SEM5 EVENTGALLERY

## Project Overview

SEM5 EVENTGALLERY is a Kubernetes-based application for managing event photo galleries with integrated image recognition using AWS Rekognition. The project demonstrates modern cloud-native practices, including container orchestration, GitOps workflows, and scalable microservices.

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