# this program runs in the background and monitors changes in the file

import os
import time

file_path = 'bg_service.py'


def check_if_file_changed(file_path, last_modified):
    if os.path.exists(file_path):
        if os.path.getmtime(file_path) != last_modified:
            return True
    return False


def get_file_last_modified(file_path):
    if os.path.exists(file_path):
        return os.path.getmtime(file_path)
    return None


def auto_compile():
    os.system("pyinstaller -f -w bg_service.py")
    os.system("bg_service.exe")


def bg_loop():
    last_modified = get_file_last_modified(file_path)
    while True:
        if check_if_file_changed(file_path, last_modified):
            print("File changed!")
            last_modified = get_file_last_modified(file_path)
        time.sleep(1)


if __name__ == '__main__':
    bg_loop()
