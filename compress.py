import os
from os import path
import gzip
import click


def check_if_path_exists(path_to_dir: str) -> bool:  # return true if path exists
    return path.exists(path_to_dir)


@click.command()
@click.option("--path", "path_to_dir", type=str, required=True,
              help="Path to directory where .log files will be compressed")
@click.option("--d", "delete_file", is_flag=True,
              help="Delete all .log files after they were gzipped.")
def gzip_logs(path_to_dir: str, delete_file: bool = False):
    if not check_if_path_exists(path_to_dir):
        print("Path do not exist")
        return

    if len(os.listdir(path_to_dir)) == 0:  # if directory is empty
        print("Directory is empty, Nothing to compress.")
        return

    for file in os.scandir(path_to_dir):

        if len(file.name) < 4 or str(file.name)[-4:] != ".log":  # if ending different from .log
            continue

        try:
            with open(file.path, "rb") as file_in:
                with gzip.open(file.path + ".gz", "wb") as file_out:
                    file_out.writelines(file_in)

            if delete_file:  # if switcher -d
                os.remove(file.path)

        except (OSError, MemoryError, PermissionError) as err:
            raise err


if __name__ == "__main__":
    gzip_logs()
