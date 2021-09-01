import os
import gzip
import sys


def check_switcher_to_delete() -> bool:  # return True, if line argument was -d

    if len(sys.argv) >= 2 and sys.argv[1] == "-d":
        print(sys.argv[1])
        return True
    return False


def gzip_logs(delete_file: bool = False):
    path_to_dir: str = "/var/skus"
    if len(os.listdir(path_to_dir)) == 0:  # if directory is empty
        print("Directory is empty, Nothing to compress.")
        return

    if check_switcher_to_delete():  # set that file will be deleted
        delete_file = True

    for file in os.scandir(path_to_dir):

        if len(file.name) < 4 or str(file.name)[-4:] != ".log":  # if ending different from .log
            continue

        print("Path to dir:", path_to_dir)

        try:
            with open(file.path, "rb") as file_in:
                with gzip.open(file.path + ".gz", "wb") as file_out:
                    print("File name", file.name)
                    file_out.writelines(file_in)

            print(file.path)
            if delete_file:  # if switcher -d
                os.remove(file.path)

        except OSError:
            print(OSError)
            return

        except MemoryError:
            print(MemoryError)
            return

def unzip_dir():
    for file in os.scandir(os.getcwd()):

        if str(file.name)[-3:] == ".gz":
            file_out = open(file.name[:-3], "w")
            with gzip.open(file.path, "rb") as file_in:
                    file_out.write(file_in.read().decode("utf-8"))

            file_out.close()

gzip_logs()
#unzip_dir()
