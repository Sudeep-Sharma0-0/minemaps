import os
import nbtlib

from copy_map import copy_to_minecraft as copy_map


def analyze_dir(dir_path):
    is_minecraft_save = check_minecraft_save(dir_path)

    if is_minecraft_save:
        version = get_version(dir_path)
        copy_map(dir_path)
        print(f"Valid Minecraft savefile of version: {version}")


def check_minecraft_save(directory):
    if not os.path.exists(directory):
        return False

    required_files = ["level.dat", "region"]
    for file in required_files:
        if not os.path.exists(os.path.join(directory, file)):
            return False

    playerdata_folder = os.path.join(directory, "playerdata")
    if not os.path.exists(playerdata_folder) or not os.listdir(playerdata_folder):
        print("Warning: 'playerdata' folder is missing or empty.")

    return True


def get_version(directory):
    if not os.path.exists(directory):
        return None

    level_dat_file = os.path.join(directory, "level.dat")
    if not os.path.exists(level_dat_file):
        return None

    try:
        level_dat = nbtlib.load(level_dat_file)
        version = level_dat["Data"]["Version"]["Name"]
        return version
    except Exception as e:
        print(f"Error reading level.dat: {e}")
        return None
