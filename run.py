from crontab import CronTab
import getpass
import os
import sys


def check_switcher_to_delete() -> bool:  # return True, if line argument was -d

    if len(sys.argv) >= 2 and sys.argv[1] == "-d":
        return True
    return False


def run_crontab():
    path: str = os.path.abspath(os.getcwd())
    path_to_file: str = path + "/compress.py"

    cron = CronTab(user=getpass.getuser())  # get current user
    if check_switcher_to_delete():
        job = cron.new(command=f'/usr/bin/python3 {path_to_file} -d')
    else:
        job = cron.new(command=f'/usr/bin/python3 {path_to_file}')

    job.setall('0 5 */30 * *')  # set every month

    cron.write()


if __name__ == "__main__":
    run_crontab()