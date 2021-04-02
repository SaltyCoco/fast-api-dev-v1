#!/bin/bash

source ../azure-deploy/azure-deploy-config.yaml

az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER_NAME