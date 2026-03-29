import subprocess

def block_ip_windows(ip_address):
    """Adds a rule to Windows Firewall to block a specific IP."""
    rule_name = f"IDS_BLOCK_{ip_address}"
    # Command: netsh advfirewall firewall add rule ...
    command = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}",
        "dir=in",
        "action=block",
        f"remoteip={ip_address}",
        "enable=yes"
    ]
    
    try:
        subprocess.run(command, check=True, shell=True)
        return f"Successfully blocked {ip_address}"
    except subprocess.CalledProcessError as e:
        return f"Failed to block {ip_address}: {e}"

# Example trigger
# block_ip_windows("192.168.1.105")