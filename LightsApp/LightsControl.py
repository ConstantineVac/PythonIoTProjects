import subprocess
from tuya_iot import TuyaOpenAPI, TUYA_LOGGER
import logging
import copy

import time

def is_iphone_connected(ip_address):
    result = subprocess.run(['ping', '-n', '1', ip_address], capture_output=True)
    print(result.stdout.decode())  # Print the output of the ping command
    return result.returncode == 0

# Replace 'iphone_ip_address' with the actual IP address of your iPhone on the local network
iphone_ip_address = '192.168.1.3'

# Replace with your actual credentials and device ID
ENDPOINT = 'https://openapi.tuyaeu.com'
ACCESS_ID = 'project_access_key'
ACCESS_KEY = 'your_projects_secret_key'
USERNAME = 'your_email.com'
PASSWORD = 'smartlife_app_password'
DEVICE_ID = 'bfddab7eb87093f958andt'

# Initialize TuyaOpenAPI
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect(USERNAME, PASSWORD, "86", 'smartlife')

# Uncomment the following line to see logs
TUYA_LOGGER.setLevel(logging.DEBUG)

# Turn the lights green or red based on iPhone connection status
while True:
    connected = is_iphone_connected(iphone_ip_address)
    print(f"Connected: {connected}")
    
    if connected:
        # Turn the lights green
        commands = {
            'commands': [
                {
                    'code': 'colour_data_v2',
                    'value': {
                        'h': 120,   # Set hue to 120 (green)
                        's': 1000,  # Set saturation to maximum
                        'v': 1000   # Set brightness to maximum
                    }
                }
            ]
        }
    else:
        # Turn the lights red
        commands = {
            'commands': [
                {
                    'code': 'colour_data_v2',
                    'value': {
                        'h': 0,     # Set hue to 0 (red)
                        's': 1000,  # Set saturation to maximum
                        'v': 1000   # Set brightness to maximum
                    }
                }
            ]
        }
    
    # Send the commands to the device
    openapi.post(f'/v1.0/devices/{DEVICE_ID}/commands', copy.deepcopy(commands))
    
    # Wait for some time before checking the iPhone connection again
    time.sleep(1)  # Adjust the delay as desired
