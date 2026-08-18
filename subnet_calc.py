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
