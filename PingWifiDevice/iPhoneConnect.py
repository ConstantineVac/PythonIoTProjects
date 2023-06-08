import subprocess

def is_iphone_connected(ip_address):
    result = subprocess.run(['ping', '-n', '1', ip_address], capture_output=True)
    print(result.stdout.decode())  # Print the output of the ping command
    return result.returncode == 0

# Replace 'iphone_ip_address' with the actual IP address of your iPhone on the local network
iphone_ip_address = '192.168.1.3'
connected = is_iphone_connected(iphone_ip_address)

print(f"Connected: {connected}")
