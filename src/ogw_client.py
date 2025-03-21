import os
from opengateway_sandbox_sdk import ClientCredentials, DeviceLocation

client_id = os.environ.get('OGW_CLIENT_ID')
client_secret = os.environ.get('OGW_CLIENT_SECRET')

if not client_id or not client_secret:
    raise ValueError("Environment variables OGW_CLIENT_ID and OGW_CLIENT_SECRET must be set")

credentials = ClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

def get_device_location_client(phone_number: str) -> DeviceLocation:
    return DeviceLocation(credentials=credentials, phone_number=phone_number)
