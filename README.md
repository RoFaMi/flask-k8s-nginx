# Flask + MySQL + Nginx en Kubernetes

Este repositorio contiene una aplicación Flask con frontend y backend, desplegada en Kubernetes con Nginx como proxy inverso.

## Estructura

- `backend/`: Aplicación Flask (API)
- `frontend/`: Cliente HTML + JS
- `k8s/`: Archivos YAML para desplegar MySQL, frontend, backend y nginx
- `.github/workflows/`: CI/CD con GitHub Actions (opcional)

## Cómo usar

```bash
kubectl apply -f k8s/mysql-deployment.yml
kubectl apply -f k8s/backend-deployment.yml
kubectl apply -f k8s/frontend-deployment.yml
kubectl apply -f k8s/nginx-config.yaml
kubectl apply -f k8s/nginx-deployment.yml
