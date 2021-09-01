import os
from os import path
import gzip
import sys


def check_switcher_to_delete() -> bool:  # return True, if line argument was -d

    if len(sys.argv) >= 2 and sys.argv[1] == "-d":
        print(sys.argv[1])
        return True
    return False


def check_if_path_exists(path_to_dir: str):
    return path.exists(path_to_dir)


def gzip_logs(path_to_dir: str, delete_file: bool = False):
    if not check_if_path_exists(path_to_dir):
        print("Path do not exists")
        return

    if len(os.listdir(path_to_dir)) == 0:  # if directory is empty
        print("Directory is empty, Nothing to compress.")
        return

    if check_switcher_to_delete():  # set that file will be deleted
        delete_file = True

    for file in os.scandir(path_to_dir):

        if len(file.name) < 4 or str(file.name)[-4:] != ".log":  # if ending different from .log
            continue

        try:
            with open(file.path, "rb") as file_in:
                with gzip.open(file.path + ".gz", "wb") as file_out:
                    file_out.writelines(file_in)

            if delete_file:  # if switcher -d
                os.remove(file.path)

        except (OSError, MemoryError) as err:
            raise err


if __name__ == "__main__":
    gzip_logs("/var/log")
