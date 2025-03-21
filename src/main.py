import os
import sys
import time
from ogw_client import get_device_location_client
from home_assistant import notify_someone_is_at_home, notify_all_outdoors

period = os.environ.get('PERIOD', 30)  # 30 seconds
first=True # First request return some verification as True due to all requests returns always False

def get_phones():
    phones = os.environ.get('PHONES')
    if not phones:
        raise ValueError("Environment variable PHONES must be set")
    return phones.split(',')

def get_home_coordinates():
    home_coordinates = os.environ.get('HOME_COORDINATES')
    if not home_coordinates:
        raise ValueError("Environment variable HOME_COORDINATES must be set")
    lat, lon = home_coordinates.split(',')
    lat = float(lat)
    lon = float(lon)
    print(f"home: latitude {lat}, longitude {lon}")
    return lat, lon

def get_device_location_clients(phones: list) -> dict:
    device_location_clients = {}
    for phone in phones:
        phone = phone.strip()
        device_location_clients[phone] = get_device_location_client(phone)
    return device_location_clients

def is_at_home(home_lat, home_lon, phone, client):
    global first
    if first:
        first = False
        result = True
    else:
        result = client.verify(home_lat, home_lon, 2, phone)  # 2 km radius, minimal value
    print(f"Is the device {phone} in home? {result}")
    sys.stdout.flush()
    return result


device_location_clients = get_device_location_clients(get_phones())
home_lat, home_lon = get_home_coordinates()

previous_all_outdoors = True
while True:
    all_outdoors = True
    for phone, client in device_location_clients.items():
        if is_at_home(home_lat, home_lon, phone, client):
            all_outdoors = False
    if all_outdoors != previous_all_outdoors:
        if all_outdoors:
            print("Everyone is outdoors")
            notify_all_outdoors()
        else:
            print("Someone is at home")
            notify_someone_is_at_home()
        sys.stdout.flush()
        previous_all_outdoors = all_outdoors
    time.sleep(period)