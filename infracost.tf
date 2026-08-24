# infracost.tf
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  # These parameters force the Azure provider to bypass live tenant validation
  skip_provider_registration = true
  
  # Crucial for offline testing: skips checking if the resource group exists live in Azure
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
}







