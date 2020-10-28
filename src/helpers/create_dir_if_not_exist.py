from typing import List
from pathlib import Path
import os


def create_dir_if_not_exist(dir_paths: List[Path]):
    print(f"Scanning for necessary directories")
    for dir_path in dir_paths:
        if os.path.exists(dir_path):
            print(f"Found directory {dir_path}")
        else:
            print(f"Creating '{dir_path}' directory at project's root")
            dir_path.mkdir(parents=True)
