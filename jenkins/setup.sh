#!/bin/bash

# Login using managed identity
# Requires managed identity to be setup for VM
az login --identity
sudo az aks install-cli
az aks get-credentials --resource-group $K8S_RESOURCE_GROUP --name $K8S_CLUSTER_NAME

# Install Ansible
# Requires pip3 to be installed
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
pip3 install -U pip
pip3 install --user ansible

# Install dependencies
~/.local/bin/ansible-playbook ansible/jenkins-setup.yaml
