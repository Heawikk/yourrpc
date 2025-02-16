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
    os.system('cls')
    print("Enter new description:")
    status = input()

    print("Enter new state:")
    stateinput = input()
    
    print("Enter image URL or press Enter for skip:")
    image_url = input()
    
    config = {
        'status': status,
        'state': stateinput,
        'image_url': image_url if image_url else None
    }
    
    save_config(config)
    
    presence.connect()
    
    if image_url:
        presence.update(details=status, state=stateinput, large_image=image_url)
    else:
        presence.update(details=status)
    
    os.system('cls')
    print(f"Status installed: {status}")

def delete_status():
    os.system('cls')
    presence.clear()
    if os.path.exists(config_file):
        os.remove(config_file)
    print("Status Removed.")

def main_menu():
    os.system('cls')
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
            os.system('cls')
            print("Invalid command, try again.")

if __name__ == '__main__':
    main_menu()