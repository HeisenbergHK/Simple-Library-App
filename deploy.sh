#!/bin/bash

set -e  # Exit if any command fails

# Step 1: Apply Kubernetes configs
echo "▶ Applying Kubernetes configs..."
kubectl apply -f k8s/

# Step 2: Wait for pods to be ready
echo "▶ Waiting for Django pods to become ready..."
kubectl rollout status deployment/django

# Step 3: Open Django service in browser (for Minikube only)
echo "▶ Launching Django service..."
minikube service django-service