# clear "work_dir"
import os, glob


def get_clear_dir_avi():
    dir_main = '/home/adrian/Pulpit/GitHub_Public/Dectenion_face/avi'

    filelistMain = glob.glob(os.path.join(dir_main, "*"))

    for files in filelistMain:
        os.remove(files)
