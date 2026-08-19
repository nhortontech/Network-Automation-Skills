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

