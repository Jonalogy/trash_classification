import random
from math import floor


def split_train_test(image_paths, train_ratio, validation_ratio):
    random.shuffle(image_paths)
    total_image_count = len(image_paths)
    train_count = floor(total_image_count * train_ratio)
    validation_count = floor(total_image_count * validation_ratio)
    test_count = total_image_count - train_count - validation_count
    print(f'Total images found: {len(image_paths)}')
    print(f'Train: {train_count}, Validation: {validation_count}, Test: {test_count}')
    return [
        image_paths[:train_count],
        image_paths[train_count: (train_count+validation_count)],
        image_paths[train_count+validation_count:]
    ]
