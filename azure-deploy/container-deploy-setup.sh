#!/bin/bash

# az acr create --name myregistry --resource-group mygroup --sku standard --admin-enabled true
az acr create --name fast-api-test-registry --resource-group testing --sku standard --admin-enabled true
az acr build --file Dockerfile --registry fast-api-test-registry --image fast-api-test:v1 .