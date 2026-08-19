import ipaddress

def generate_lab_subnets(base_network_str):
    print(f"⚙️ Parsing Base Network Infrastructure Block: {base_network_str}\n")
    
    try:
        base_net = ipaddress.ip_network(base_network_str)
        subnets = list(base_net.subnets(new_prefix=24))
        
        lab_architecture = {
            "10.0.1.0/24": "Management-Subnet (Firewall GUI Backdoor Port)",
            "10.0.2.0/24": "Untrust-Subnet (Outside Facing Internet Traffic)",
            "10.0.3.0/24": "Trust-Subnet (Inside Secure Linux Workloads)"
        }
        
        print(f"📝 DESIGN METRICS FOR YOUR AZURE LAB RESILIENCE:")
        print("=" * 65)
        
        for net in subnets[:3]:
            net_str = str(net)
            purpose = lab_architecture.get(net_str, "Available Spare Subnet Pool")
            
            hosts = list(net.hosts())
            first_usable = hosts[0]
            last_usable = hosts[-1]
            broadcast = net.broadcast_address
            
            print(f"🎯 Zone Allocation: {purpose}")
            print(f"   🔹 Network ID:      {net.network_address}")
            print(f"   🔹 Subnet Mask:    {net.netmask}")
            print(f"   🔹 Gateway/First:   {first_usable} (Assign to Firewall Interface)")
            print(f"   🔹 Usable Range:   {first_usable} --> {last_usable}")
            print(f"   🔹 Broadcast IP:   {broadcast}")
            print("-" * 65)
            
    except ValueError as e:
        print(f"⚠️ Operation Aborted: Invalid CIDR notation format input. {str(e)}")

generate_lab_subnets("10.0.0.0/16")






# PRODUCTION LEVEL VERSION:

import os
import ipaddress
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.models import VirtualNetwork, Subnet

def deploy_azure_network(subscription_id, resource_group, vnet_name, base_network_str):
    print(f"🚀 Initializing Live Azure Network Pipeline for block: {base_network_str}")
    
    try:
        # 1. Standardize Authentication using your Azure Login credentials
        credential = DefaultAzureCredential()
        network_client = NetworkManagementClient(credential, subscription_id)
        
        # 2. Execute your core subnet routing math programmatically
        base_net = ipaddress.ip_network(base_network_str)
        calculated_subnets = list(base_net.subnets(new_prefix=24))
        
        # 3. Map your architecture zones dynamically to CIDR blocks
        subnet_definitions = [
            Subnet(name="Management-Subnet", address_prefix=str(calculated_subnets[1])), # 10.0.1.0/24
            Subnet(name="Untrust-Subnet",    address_prefix=str(calculated_subnets[2])), # 10.0.2.0/24
            Subnet(name="Trust-Subnet",      address_prefix=str(calculated_subnets[3]))  # 10.0.3.0/24
        ]
        
        # 4. Construct the complete Virtual Network parameter block
        vnet_params = VirtualNetwork(
            location="australiaeast",
            address_space={"address_prefixes": [base_network_str]},
            subnets=subnet_definitions
        )
        
        # 5. Push the configuration matrix to the Microsoft API
        print(f"📡 Provisioning VNet [{vnet_name}] and 3 secure subnets in Azure...")
        async_vnet_creation = network_client.virtual_networks.begin_create_or_update(
            resource_group,
            vnet_name,
            vnet_params
        )
        
        # Wait for the cloud data center to finish building the infrastructure
        async_vnet_creation.wait()
        print("✅ SUCCESS: Your Palo Alto network fabric is live in Azure!")
        
    except Exception as e:
        print(f"❌ Deployment Aborted: {str(e)}")

# 🏃‍♂️ RUN ENVIRONMENT CONFIGURATION (Update with your home parameters)
AZURE_SUBSCRIPTION_ID = "your-azure-subscription-id-here"
LAB_RESOURCE_GROUP    = "rg-paloalto-lab"
LAB_VNET_NAME         = "vnet-paloalto"

deploy_azure_network(AZURE_SUBSCRIPTION_ID, LAB_RESOURCE_GROUP, LAB_VNET_NAME, "10.0.0.0/16")


# TERMINAL COMMANDS:

pip install azure-identity azure-mgmt-network
az login
python subnet_calc.py
