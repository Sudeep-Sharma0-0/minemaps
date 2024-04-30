import shutil


def copy_to_minecraft(dir):
    shutil.move(
        dir, "/games/Minecraft/instances/Create Optimized [FABRIC]/minecraft/saves/")
