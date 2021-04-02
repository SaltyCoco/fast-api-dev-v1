#!/bin/bash

# Look into API Management

# Source Variables File
source ../azure-deploy/azure-deploy-config.yaml

# Before you can do anything you need to login into Azure
az login
# if web browser fails: alternative way to login
az login --use-device-code

# Create a resource group.
az group create --location westus --name "$RESOURCE_GROUP" --subscription "$SUB_ID"
# List groups
az group list --output table
# Query resource groups and get back info
az group list --query "[?name == '$RESOURCE_GROUP']"

# ACR Setup
az acr create --name "$REGISTRY_NAME" --resource-group "$RESOURCE_GROUP" --sku "$ACR_SKU" --admin-enabled true
az acr repository list --name "$REGISTRY_NAME" --resource-group "$RESOURCE_GROUP"

# Build container for Azure
az acr login --name "$REGISTRY_NAME"
az acr build --file Dockerfile --registry "$REGISTRY_NAME" --image "$IMAGE_NAME" .
az acr repository list --name "$REGISTRY_NAME" --resource-group "$RESOURCE_GROUP"

# Build Web App
az webapp create --name "$WEBAPPNAME" --resource-group "$RESOURCE_GROUP"  --subscription "$SUB_ID"  --plan "$ACR_PLAN" --location westus