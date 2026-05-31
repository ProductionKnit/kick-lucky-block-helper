import json
import os

DEFAULT_CONFIG = {
    "scan_interval": 5,
    "detection_chance": 0.1,
    "webhook_url": "",
    "auto_kick": False
}

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r") as f:
                config = json.load(f)
            return {**DEFAULT_CONFIG, **config}
        except (json.JSONDecodeError, IOError):
            print("Config file corrupted, using defaults")
            return DEFAULT_CONFIG.copy()
    else:
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)