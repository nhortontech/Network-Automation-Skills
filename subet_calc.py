import ipaddress
def generate_lab_subnets(base_network_str):
    print(f"Parsing Base Network Infrastructure Block: {base-network_str}\n")

    try:
        #1. Instantiate the core neqtwork block object
        base_net = ipaddress.ip_network(base_network_str)

        #2. Slice main block into standard /24 subnets cleanly
        subnets = list(base_net.subnets(new_prefix=24))

        #3. Map subnets out to specific Azure.Palo Alto lab tiers
        lab_architecture = {
            "10.0.1.0/24": "Managaement-Subnet (Firewall GUI Backdoor Port)",
            "10.0.2.0/24": "Untrust-Subnet (Outside Facing Internet Traffic)",
            "10.0.3.0/24": "Trust-Subnet (Inside Secure Linux Workloads)"
        }

        print(f"Design Metrics for your Azure Lab resilience:")
        print("=" * 65)

        #4. Loop through generated allocations and calculate gateway rules
        for net in subnets[:3]:
            net_str = str(net)
            purpose = lab_architecture.get(net_str, "Available Spare Subnet Pool")

            # Extract usable boundary hosts matching parameters (CCNA)
            hosts = list(net.hosts())
            first_usable = hosts[0]
            last_usable = hosts[-1]
            broadcast = net.broadcast_address

            print(f"Zone Allocation: {purpose}")
            print(f"Network ID: {net.network_address}")
            print(f"Subnet Mask: {net.netmask}")
            print(f"Gateway/First: {first_usable} (Assign to Firewall Interface)")
            print(f"Usable Range: {first_usable} --> {last_usable}")
            print(f"Briadcast IP: {broadcast}")
            print("-" * 65)

    except ValueError as e:
        print(f"Operation Aborted: Invalid CIDR notation format input. {str(e)}")

# Trigger execution using standard class A deployment block
# generate_lab_subnets("10.0.0.0/16") 

