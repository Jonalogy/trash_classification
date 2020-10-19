import shutil
import os
from .partition import partition


def split_train_valid_test(image_directory, train_dir, valid_dir, test_dir, train_ratio, valid_ratio):
    for class_name in image_directory.iterdir():
        if class_name.is_dir():
            # ensures class directories exists in train and test directories
            for t in [train_dir, valid_dir, test_dir]:
                if not os.path.exists(t / class_name.name):
                    os.mkdir(t / class_name.name)

            image_list = list(class_name.glob('*.jpg'))
            train_list, valid_list, test_list = partition(image_list, train_ratio, valid_ratio)

            print(f'Copying {len(train_list)} of {len(image_list)} to {train_dir / class_name.name}')
            for file in train_list:
                target = str(image_directory / class_name.name / file.name)
                dest = str(train_dir / class_name.name / file.name)
                shutil.copyfile(target, dest)

            print(f'Copying {len(valid_list)} of {len(image_list)} to {valid_dir / class_name.name}')
            for file in valid_list:
                target = str(image_directory / class_name.name / file.name)
                dest = str(valid_dir / class_name.name / file.name)
                shutil.copyfile(target, dest)

            print(f'Copying {len(test_list)} of {len(image_list)} to {test_dir / class_name.name}')
            for file in test_list:
                target = str(image_directory / class_name.name / file.name)
                dest = str(test_dir / class_name.name / file.name)
                shutil.copyfile(target, dest)
