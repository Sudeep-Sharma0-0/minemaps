import os
import zipfile


def extract_zip(filename):
    folder_to_extract = os.path.dirname(filename)
    with zipfile.ZipFile(filename, "r") as zip_ref:
        root_dir = None
        for name in zip_ref.namelist():
            if "/" not in name:
                root_dir = ""
                break
            dir_name = name.split("/")[0]
            if root_dir is None:
                root_dir = dir_name
            elif root_dir != dir_name:
                root_dir = ""
                break

        if root_dir:
            zip_ref.extractall(folder_to_extract)
            print(
                f"Extracted zip file {filename} preserving directory structure")
        else:
            container_dir = os.path.splitext(os.path.basename(filename))[0]
            container_path = os.path.join(folder_to_extract, container_dir)
            os.makedirs(container_path, exist_ok=True)
            zip_ref.extractall(container_path)
            print(
                f"Extracted zip file {filename} into container directory {container_path}")
