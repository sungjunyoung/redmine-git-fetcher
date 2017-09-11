import argparse
import os
import subprocess


def parse_args():
    desc = "redmine git fetcher :: to use, you must add to crontab"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--git_dir', type=str, help='directory that includes .git folders', required=True)

    return parser.parse_args()

def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

def main():
    args = parse_args()
    if args is None:
        exit()

    # git_dir not exist
    if not os.path.exists(args.git_dir):
        print("ERROR::" + args.git_dir, " not exist!")
        exit()

    for root, folders, files in os.walk(args.git_dir, topdown=False):
        if len(folders) == 0:  # if folders length is 0, continue
            continue
        if all(str[-4:] != '.git' for str in folders):  # if not git folder, continue
            continue

        for git in folders:
            cd_command = ['cd',root + '/' + git]
            run_command(cd_command)
            fetch_command = ['git', 'fetch', '-a']
            for line in run_command(fetch_command):
                print(line)


if __name__ == '__main__':
    main()
