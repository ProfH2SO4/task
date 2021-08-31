import os
import gzip

path_to_dir: str = "/home/matej/PycharmProjects/task/log"


def gzip_directory():
    if len(os.listdir(path_to_dir)) == 0:  # if directory is empty
        print("Directory is empty, Nothing to compress.")
        return


    for file in os.scandir(path_to_dir):
        try:
            if str(file.name)[-3:] == ".gz":  # if file already compressed, skip
                continue

            with open(file.path, "rb") as file_in:
                with gzip.open(file.name + ".gz", "wb") as file_out:
                    file_out.writelines(file_in)
                print(file.path)

        except OSError:
            print(OSError)
            return


def unzip_dir():
    for file in os.scandir(os.getcwd()):

        if str(file.name)[-3:] == ".gz":
            file_out = open(file.name[:-3], "w")
            with gzip.open(file.path, "rb") as file_in:
                    file_out.write(file_in.read().decode("utf-8"))

            file_out.close()

gzip_directory()
#unzip_dir()
