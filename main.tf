# Define Local Variables for Azure Palo Alto Lab Topology
locals {
    resource_group = "rg-paloalto-lab"
    region         = "Australia East"
    vm_size        = "Standard_D8as_v7" # 8-core size that unlocks NIC limits

    subnets = {
        management = "10.0.1.0/24"
        untrust    = "10.0.2.0/24"
        trust      = "10.0.3.0/24"
    }
}

# Use local provider to build automated deployment doc
resource "local_file" "network_manifest" {
    filename = "${path.module}/azure_deployment_manifest.txt"
    content = <<-EOT

Target Resource Group: ${local.resource_group}
Target Azure Region:   ${local.region}
Firewall Core Compute: ${local.vm_size}

nic0 (MGMT):    ${local.subnets.management}
nic1 (UNTRUST): ${local.subnets.untrust}
nic2 (TRUST):   ${local.subnets.trust}

Generated on: 2026-08-19 (Local Cloud Run)

EOT
}




# PRODUCTION LEVEL VERSION:

# 1. TELL TERRAFORM TO LOAD THE OFFICIAL MICROSOFT AZURE API PLUGINS
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {} # Activates default Azure API connection rules
}

# PROVISION YOUR REAL AZURE LAB RESOURCE GROUP
resource "azurerm_resource_group" "lab_rg" {
  name     = "rg-paloalto-lab"
  location = "Australia East"
}

# PROVISION YOUR UNIFIED LAB VIRTUAL NETWORK (VNET)
resource "azurerm_virtual_network" "paloalto_vnet" {
  name                = "vnet-paloalto"
  location            = azurerm_resource_group.lab_rg.location
  resource_group_name = azurerm_resource_group.lab_rg.name
  address_space       = ["10.0.0.0/16"]
}

# CARVE OUT YOUR INFRASTRUCTURE SECURITY ZONE SUBNETS AUTOMATICALLY
resource "azurerm_subnet" "mgmt_subnet" {
  name                 = "management-subnet"
  resource_group_name  = azurerm_resource_group.lab_rg.name
  virtual_network_name = azurerm_virtual_network.paloalto_vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_subnet" "untrust_subnet" {
  name                 = "untrust-subnet"
  resource_group_name  = azurerm_resource_group.lab_rg.name
  virtual_network_name = azurerm_virtual_network.paloalto_vnet.name
  address_prefixes     = ["10.0.2.0/24"]
}

resource "azurerm_subnet" "trust_subnet" {
  name                 = "trust-subnet"
  resource_group_name  = azurerm_resource_group.lab_rg.name
  virtual_network_name = azurerm_virtual_network.paloalto_vnet.name
  address_prefixes     = ["10.0.3.0/24"]
}

# TERMINAL COMMANDS:

# terraform init
# az login
# terraform apply