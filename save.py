import os
import pickle
from rich.console import Console
from AddressBook import *
from rich.console import Console
from classes import *
from bot import Bot
from bot import *



def list_backups(directory_path: str) -> None:
    backup_folder = os.path.join(directory_path, "backup")
    if not os.path.exists(backup_folder):
        print("No backups available.")
        return
    
    backup_files = [f for f in os.listdir(backup_folder) if os.path.isfile(os.path.join(backup_folder, f))]
    if backup_files:
        print("Available backups:")
        for file in backup_files:
            print(file)
    else:
        print("No backups available.")

def restore_from_backup(directory_path: str, backup_file: str, address_book: AddressBook) -> None:
    backup_path = os.path.join(directory_path, "backup", backup_file)
    if not os.path.exists(backup_path):
        print("Backup file not found.")
        return
    
    with open(backup_path, "rb") as backup_file:
        backup_data = pickle.load(backup_file)
        address_book.data = backup_data
        address_book.save_to_file()
        print("Data restored from backup successfully.")







