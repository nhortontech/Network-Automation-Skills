import sys
from netmiko import ConnectHandler
from paramiko.ssh_exception import SSHException

# Target the local Linux container shell instead of external Cisco sandboxes
local_node = {
    'device_type': 'terminal_server',
    'host': '127.0.0.1', # loopback network IP
    'username': 'codespace',
    'password': 'codespace',
    'allow_agent': False,
    'read_timeout_override': 5,
}

print("Establishing secure encrypted SSH pipeline to Cisco Edge Core...")

try:
    # Open the dynamic transport pipeline
    net_connect = ConnectHandler(**local_node)

    # Execute the Linux analysis commands directly (REMOVED .enable() line
    output = net_connect.send_command('uname -a && df -h')

    print("\n Target Metrics Retrieved Successfully:")
    print("-" * 50)
    print(output)
    print("-" * 50)

    # Clean up connection
    net_connect.disconnect()

except SSHException:
    print("Security Handshake Failed: SSH configuration dropped.")
except Exception as e:
    print(f"Operation Aborted: {str(e)}")




# PRODUCTION LEVEL VERSION:

# import sys
# from netmiko import ConnectHandler
# from paramiko.ssh_exception import SSHException

# Target your live Azure Palo Alto Firewall Appliance
# paloalto_fw_node = {
#     'device_type': 'paloalto_panos',     # Loads the explicit PAN-OS syntax drivers
#     'host': '20.211.43.215',             # Your firewall's static public Azure IP
#     'username': 'paloadmin',             # The admin user you built in the portal
#     'password': 'YourSecurePassword123!', # Your actual firewall login password
#     'port': 22,                          # Standard SSH management port
# }

# print("🚀 Establishing secure encrypted SSH pipeline to Azure Palo Alto Perimeter...")

# try:
#     # Open the dynamic transport pipeline across the internet
#     net_connect = ConnectHandler(**paloalto_fw_node)

#     # Execute native PAN-OS operational commands to inspect health metrics
#     # 'show system info' pulls serial numbers, uptime, and software versions
#     output = net_connect.send_command('show system info')

#     print("\n🔥 FIREWALL METRICS RETRIEVED SUCCESSFULLY:")
#     print("-" * 60)
#     print(output)
#     print("-" * 60)

#     # Clean up connection to prevent stale management sessions
#     net_connect.disconnect()

# except SSHException:
#     print("❌ Security Handshake Failed: SSH configuration dropped by perimeter.")
# except Exception as e:
#     print(f"⚠️ Operation Aborted: {str(e)}")

