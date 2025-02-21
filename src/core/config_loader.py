# src/core/config_loader.py
import yaml
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent.parent / 'config' / 'servers.yaml'
    with open(config_path) as f:
        return yaml.safe_load(f)
