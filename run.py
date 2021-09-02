from crontab import CronTab
import getpass
import os
import click


@click.command()
@click.option("--path", "path_to_dir", type=str, required=True,
              help="Path to directory where .log files will be compressed")
@click.option("--d", "delete_file", is_flag=True,
              help="Delete all .log files after they were gzipped.")
def run_crontab(path_to_dir: str, delete_file: bool = False):
    path: str = os.path.abspath(os.getcwd())
    path_to_file: str = path + "/compress.py"

    cron = CronTab(user=getpass.getuser())  # get current user
    if delete_file:
        job = cron.new(command=f"/usr/bin/python3 {path_to_file} --path {path_to_dir} --d")
    else:
        job = cron.new(command=f"/usr/bin/python3 {path_to_file} --path {path_to_dir}")

    job.setall("0 5 */30 * *")  # set every month

    cron.write()


if __name__ == "__main__":
    run_crontab()