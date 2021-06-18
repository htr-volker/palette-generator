#!/bin/bash
if [ -z $BRANCH_NAME ];
then
    BRANCH_NAME="default"
fi
echo "Namespace: ${BRANCH_NAME}"
kubectl create namespace $BRANCH_NAME || true
kubectl apply -f k8s --namespace=$BRANCH_NAME