import random


def split_train_test(image_paths, train_ratio):
    random.shuffle(image_paths)
    total_image_count = len(image_paths)
    train_count = round(total_image_count * train_ratio)
    test_count = total_image_count - train_count
    print(f'total: {len(image_paths)}, train: {train_count}, test:{test_count}')
    return [image_paths[:train_count], image_paths[train_count:]]
