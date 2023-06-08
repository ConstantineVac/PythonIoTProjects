from tuya_iot import TuyaOpenAPI, TUYA_LOGGER
import logging

# Replace with your actual credentials and device ID
ENDPOINT = 'https://openapi.tuyaeu.com'
ACCESS_ID = 'anmthpjcekt8nexypsg4'
ACCESS_KEY = 'bbe553581af24027846b57da644b1673'
USERNAME = 'www.dragon-fire@hotmail.com'
PASSWORD = 'Kostas98'
DEVICE_ID = 'bfddab7eb87093f958andt'

# Initialize TuyaOpenAPI
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect(USERNAME, PASSWORD, "86", 'smartlife')

# Uncomment the following lines to see logs
TUYA_LOGGER.setLevel(logging.DEBUG)

# Toggle the light switch
flag = True
while True:
    input('Hit Enter to toggle light switch.')
    flag = not flag
    commands = {'commands': [{'code': 'switch_led', 'value': flag}]}
    openapi.post(f'/v1.0/devices/{DEVICE_ID}/commands', commands)
