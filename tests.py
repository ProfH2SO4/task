

import compress as compress
import os
import unittest
import gzip
import filecmp


# creates .log file
def create_file(path: str):
    with open(path, 'w') as file_in:
        file_in.write("ahoj")


# creates no_delete.txt file
def create_no_delete(path: str):
    with open(path, 'w') as file_in:
        file_in.write("I cannot be deleted")


def unzip_dir(path_to_dir: str):
    for file in os.scandir(path_to_dir):

        if str(file.name)[-3:] == ".gz":
            file_out = open(path_to_dir + "/unziped" + file.name[:-3], "w")
            with gzip.open(file.path, "rb") as file_in:
                file_out.write(file_in.read().decode("utf-8"))

            file_out.close()


def remove_content_in_dir(path_to_dir: str):
    for file in os.scandir(path_to_dir):
        os.remove(file)


#  checks if .log file 1.log was deleted and there should be only .gz file
#  and no_delete.txt file
def check_if_log_deleted(path_to_dir: str):
    log_count: int = 0
    gz_files_count: int = 0

    for file in os.scandir(path_to_dir):
        if file.name == "1.log.gz":
            gz_files_count += 1

        if str(file.name)[-4:] == ".log":
            log_count += 1

    return log_count == 0 and gz_files_count == 1 and len(os.listdir(path_to_dir)) == 2


class TestCompress(unittest.TestCase):

    def test_path_not_exists(self):
        path: str = os.path.abspath(os.getcwd())
        returned_bool = compress.check_if_path_exists(path + "/no_file")
        self.assertFalse(False, returned_bool)

    def test_path_exists(self):
        path: str = os.path.abspath(os.getcwd())
        returned_bool: bool = compress.check_if_path_exists(path + "/test_files")
        self.assertTrue(True, returned_bool)

    def test_check_if_compressed_same_result(self):
        path: str = os.path.abspath(os.getcwd())
        path_to_file = path + "/test_files/1.log"
        path_to_dir = path + "/test_files"
        create_file(path_to_file)
        compress.gzip_logs(path_to_dir)

        unzip_dir(path_to_dir)
        two_files_values: bool = filecmp.cmp(path_to_file, path_to_dir + "/unziped1.log")
        self.assertTrue(True, two_files_values)
        remove_content_in_dir(path_to_dir)  # delete content in test/files

    #  simulating 1.log file and no_delete.txt in /test_files
    # return true only if in test_files is 1.log.gz and no_delete.txt
    # 1.log should be deleted
    def test_switcher_delete_in_line_argument(self):
        path: str = os.path.abspath(os.getcwd())
        path_to_file = path + "/test_files/1.log"
        path_to_dir = path + "/test_files"
        create_file(path_to_file)
        compress.gzip_logs(path_to_dir, True)  # True to simulate -d parser
        create_no_delete(path_to_dir + "/no_delete.txt")
        self.assertTrue(True, check_if_log_deleted(path_to_dir))

        remove_content_in_dir(path_to_dir)  # delete content in test/files

if __name__ == "__main__":
    unittest.main()
