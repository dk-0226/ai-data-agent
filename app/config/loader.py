import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class ConfigLoader:
    def __init__(self, env: str = None):
        self.env = env or os.getenv("ENV", "dev")
        self.base_path = Path(__file__).parent

    def load_yaml(self,file_path):
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
        
    def merge_dicts(self, base, override):
        for k,v in override.items():
            if isinstance(v, dict) and k in base:
                base[k] = self.merge_dicts(base.get(k, {}), v)
            else:
                base[k] = v
        return base
    
    def load(self):
        base_config = self.load_yaml(self.base_path / "base.yaml")

        env_file = self.base_path / f"{self.env}.yaml"
        if env_file.exists():
            env_config = self.load_yaml(env_file)
            final_config = self.merge_dicts(base_config, env_config)
        else:
            final_config = base_config

        return final_config


def get_raw_config():
    loader = ConfigLoader()
    return loader.load()

from .schema import AppConfig


def get_config():
    raw_config = get_raw_config()
    return AppConfig(**raw_config)


