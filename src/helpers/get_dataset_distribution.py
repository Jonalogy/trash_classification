import os
from .get_image_count import get_image_count


def get_dataset_distribution(ds_path):
    (root, dir, files) = next(os.walk(ds_path))
    dist = dict()
    for clazz in dir:
        count = get_image_count(os.path.join(root, clazz))
        dist[f'{clazz}'] = count
    return dist
