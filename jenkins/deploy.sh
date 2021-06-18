#!/bin/bash
echo "Namespace: ${NAMESPACE}"
kubectl create namespace $NAMESPACE || true
kubectl apply -f k8s --namespace=$NAMESPACE