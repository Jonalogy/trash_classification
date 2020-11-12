import os
from pathlib import Path
from zipfile import ZipFile


def zip_dir(src_dir: str, dst_dir: str = None):
    """
    A helper method to zip a directory with the directory name
    args:
        src_dir (Str): The directory to be zipped
        dst_dir (Str): Optional. Path of the destination folder.
    """
    zip_name = str(Path(src_dir)).split("/")[-1]

    file_path = []
    for root, directories, files in os.walk(src_dir):
        for filename in files:
            str_idx = root.find(zip_name)
            file_path.append(
                (os.path.join(root, filename),  # absolute path to file on filesystem
                 os.path.join(root[str_idx:], filename))  # Desired relative path of file within zip
            )

    zip_to = f'{zip_name}.zip' if not dst_dir else f'{dst_dir}/{zip_name}.zip'
    with ZipFile(zip_to, 'w') as zip_obj:
        for (absolute_path, relative_to_zip_path) in file_path:
            zip_obj.write(absolute_path, relative_to_zip_path)
