import json
import os
import time

from pypresence import Presence
from id import settings

CLIENT_ID = (settings['id'])
presence = Presence(CLIENT_ID)

config_file = 'status_config.json'

def load_config():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(config_file, 'w') as f:
        json.dump(config, f)

def set_status():
    print("Enter new status:")
    status = input()
    
    print("Enter image URL or press Enter for skip:")
    image_url = input()
    
    config = {
        'status': status,
        'image_url': image_url if image_url else None
    }
    
    save_config(config)
    
    presence.connect()
    
    if image_url:
        presence.update(details=status, state='', large_image=image_url)
    else:
        presence.update(details=status)
    
    print(f"Status installed: {status}")

def delete_status():
    presence.clear()
    if os.path.exists(config_file):
        os.remove(config_file)
    print("Status Removed.")

def main_menu():
    while True:
        print("YourRPC 1.0.0\n\n1) Set Status\n2) Remove Status\n3) Exit")
        choice = input()
        
        if choice == '1':
            set_status()
        elif choice == '2':
            delete_status()
        elif choice == '3':
            presence.clear()
            break
        else:
            print("Invalid command, try again.")

if __name__ == '__main__':
    main_menu()