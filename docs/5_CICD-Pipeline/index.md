---
layout: default
title: 5. CI/CD-Pipeline
nav_order: 5
has_children: no
---

# 5. CI/CD-Pipeline

Die CI/CD-Pipelines der **EventGallery**-Applikation automatisieren den gesamten Prozess von der Codeänderung bis hin zur Bereitstellung auf Kubernetes. Hierbei gibt es separate Pipelines für das Backend und das Frontend.

---

## Backend CI/CD-Pipeline

### Übersicht
Die Backend-Pipeline durchläuft folgende Schritte:

1. **Code-Checkout:** Klonen des Repositories.
2. **Build und Tests:** Installation von Abhängigkeiten und Ausführen von Unit-Tests.
3. **Docker-Build:** Erstellung und Push des Docker-Images zum GitHub Container Registry (GHCR).
4. **Kubernetes-Update:** Aktualisierung der Kubernetes-Manifestdateien.

### Workflow

[Backend CI/CD Pipeline](https://github.com/noluchs/SEM4-EVENTGALLERY/blob/main/.github/workflows/backend-deploy.yml)

```yaml
name: Backend CI/CD Pipeline

on:
  push:
    paths:
      - 'code/backend/**'
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: write
  packages: write

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          cache: 'pip'
      - name: Install dependencies
        run: |
          cd code/backend
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        id: tests
        continue-on-error: true
        run: |
          cd code/backend
          python -m pytest
      - name: Notify test failures
        if: steps.tests.outcome == 'failure'
        run: |
          echo "::warning ::Tests failed but continuing with deployment"

  package-and-push:
    needs: build-and-test
    if: always()
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: docker/setup-buildx-action@v2
      - uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GHCR_TOKEN }}
      - name: Build and push backend Docker image
        run: |
          REPO_NAME=$(echo ${{ github.repository }} | tr '[:upper:]' '[:lower:]')
          docker buildx build --platform linux/amd64 \
            -t ghcr.io/$REPO_NAME/eventgallery-backend:latest \
            -t ghcr.io/$REPO_NAME/eventgallery-backend:${{ github.sha }} \
            -f ./code/backend/Dockerfile ./code/backend --push

  update-k8s:
    needs: package-and-push
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Update K8s manifests
        run: |
          REPO_NAME=$(echo ${{ github.repository }} | tr '[:upper:]' '[:lower:]')
          sed -i "s|ghcr.io/$REPO_NAME/eventgallery-backend:.*|ghcr.io/$REPO_NAME/eventgallery-backend:${{ github.sha }}|" infrastructure/k8s/backend-deployment.yaml
      - name: Commit and push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add infrastructure/k8s/backend-deployment.yaml
          git commit -m "Update backend deployment image to ${{ github.sha }}"
          git push
```

---

## Frontend CI/CD-Pipeline

### Übersicht
Die Frontend-Pipeline durchläuft folgende Schritte:

1. **Code-Checkout:** Klonen des Repositories.
2. **Build und Tests:** Installation von Abhängigkeiten und Ausführen von Tests.
3. **Docker-Build:** Erstellung und Push des Docker-Images zum GitHub Container Registry (GHCR).
4. **Kubernetes-Update:** Aktualisierung der Kubernetes-Manifestdateien.

### Workflow

[Frontend CI/CD Pipeline](https://github.com/noluchs/SEM4-EVENTGALLERY/blob/main/.github/workflows/frontend-deploy.yml)

```yaml
name: Frontend CI/CD Pipeline

on:
  push:
    paths:
      - 'code/frontend/**'
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: write
  packages: write

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
          cache-dependency-path: code/frontend/package-lock.json
      - name: Install dependencies
        working-directory: ./code/frontend
        run: npm ci
      - name: Run tests
        id: tests
        continue-on-error: true
        working-directory: ./code/frontend
        run: |
          if [ -f "package.json" ]; then
            if npm run test 2>/dev/null; then
              echo "Tests passed"
            else
              echo "::warning ::Tests failed but continuing with deployment"
            fi
          else
            echo "::warning ::No package.json found, skipping tests"
          fi

  package-and-push:
    needs: build-and-test
    if: always()
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GHCR_TOKEN }}
      - name: Build and push frontend Docker image
        run: |
          REPO_NAME=$(echo ${{ github.repository }} | tr '[:upper:]' '[:lower:]')
          docker buildx build --platform linux/amd64 \
            -t ghcr.io/$REPO_NAME/eventgallery-frontend:latest \
            -t ghcr.io/$REPO_NAME/eventgallery-frontend:${{ github.sha }} \
            -f ./code/frontend/Dockerfile.prod ./code/frontend --push

  update-k8s:
    needs: package-and-push
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Update K8s manifests
        run: |
          REPO_NAME=$(echo ${{ github.repository }} | tr '[:upper:]' '[:lower:]')
          sed -i "s|ghcr.io/$REPO_NAME/eventgallery-frontend:.*|ghcr.io/$REPO_NAME/eventgallery-frontend:${{ github.sha }}|" infrastructure/k8s/frontend-deployment.yaml
      - name: Commit and push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add infrastructure/k8s/frontend-deployment.yaml
          git commit -m "Update deployment images to ${{ github.sha }}"
          git push
```

---
