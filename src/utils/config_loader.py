# src/utils/config_loader.py
import yaml
from pathlib import Path

def load_config():
    config_path = Path(__file__).resolve().parent.parent.parent / 'config' / 'servers.yaml'
    
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
