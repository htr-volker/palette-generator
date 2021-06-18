#!/bin/bash
if [ -z $BRANCH_NAME ]
do
    BRANCH_NAME="default"
done
echo "Namespace: ${BRANCH_NAME}"
kubectl create namespace $BRANCH_NAME || true
kubectl apply -f k8s --namespace=$BRANCH_NAME