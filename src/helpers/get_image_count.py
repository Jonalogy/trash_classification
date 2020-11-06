import os
from glob import glob


def get_image_count(dir_path):
    images = []
    for ext in ['*.jpeg', '*.jpg', '*.png']:
        images = images + glob(os.path.join(dir_path, ext))
    return len(images)
