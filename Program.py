import sys
import os

def app_folder(prog: str) -> str:
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            raise

    if sys.platform == "win32":
        folder = os.path.join(os.path.expanduser("~"), "AppData", "Local", prog)
        createFolder(folder)
        return folder
    else:
        folder = os.path.join(os.path.expanduser("~"), "." + prog)
        createFolder(folder)
        return folder