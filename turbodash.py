import os
import shutil
import json
import socket

from pathlib import Path

CONFIG_FILE = "turbodash_config.json"

def load_config():
    """Load configuration from JSON file."""
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError("Configuration file not found.")
    with open(CONFIG_FILE, 'r') as file:
        return json.load(file)

def save_config(config):
    """Save configuration to JSON file."""
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)

def get_shortcuts_path():
    """Get the path to the desktop shortcuts."""
    return Path.home() / "Desktop"

def sync_shortcuts(config):
    """Synchronize shortcuts based on configuration."""
    source_device = config["devices"].get(socket.gethostname())
    if not source_device:
        raise ValueError("Current device not configured.")

    source_path = Path(source_device["path"])
    target_devices = [d for n, d in config["devices"].items() if n != socket.gethostname()]

    for device in target_devices:
        target_path = Path(device["path"])
        for item in source_path.iterdir():
            if item.is_file() and item.suffix == '.lnk':
                shutil.copy(item, target_path / item.name)
                print(f"Copied {item.name} to {device['name']}")

def main():
    try:
        config = load_config()
        sync_shortcuts(config)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()