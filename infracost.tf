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







# FOR USE AT HOME:

/*
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "test" {
  name     = "infracost-test-rg"
  location = "eastus"
}

resource "azurerm_linux_virtual_machine" "test_vm" {
  name                = "test-palo-vm"
  resource_group_name = azurerm_resource_group.test.name
  location            = azurerm_resource_group.test.location
  size                = "Standard_D2s_v5" # We will change this size later to test the diff
  admin_username      = "adminuser"
  
  network_interface_ids = [
    "mock-nic-id-for-testing"
  ]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
}
*/




