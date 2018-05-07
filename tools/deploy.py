#!/usr/bin/env python3

# Requires pygit2 (pip install pygit2)
import sys
import os
import configparser
import git

# get script path
root_path = os.path.dirname(os.path.realpath(''))
os.chdir(root_path)
# Config
config = configparser.ConfigParser()


def getConfig():
    exist = config.read('tools\\deploy.ini')
    if exist != '':
        return True
    else:
        return False

def getContent():
    return content

def main():
    # Info
    print('MD4 Deploy')
    print('This is a automated deploy script written for MD4 a Hearts of Iron 4 modification.')
    print('Written by: Andreas Brostrom | Evul <andreas.brostrom.ce@gmail.com>\n')

    # Check for config
    if not getConfig():
        sys.exit("No config is found")

    # Get reposetory link
    HTTPS = config.get('GIT', 'HTTPS', fallback='')
    print(' Reposetory:          {}'.format(HTTPS))

    # get current branch
    git_path = root_path + '\\.git'
    repo = git.Repo(git_path)
    repo = repo.active_branch
    print(' Current branch:      {}'.format(repo))

    # Check if branch is remote as well
    # To do

    # Fetching blacklist
    blacklist_list = []
    blacklist = config.get('COMMON', 'blacklist')
    for object in blacklist.split(', '):
        blacklist_list.append(object)

    # Checking files
    filter_list_dir = []
    filter_list_files = []
    for root, dirs, files in os.walk("."):
        for dirnames in dirs:
            if dirnames not in blacklist_list:
                filter_list_dir.append(dirnames)
        for filename in files:
            if filename not in blacklist_list:
                filter_list_files.append(filename)
        break
    print(filter_list_dir)
    print(filter_list_files)
    filter_list_dir_nr = len(filter_list_dir)
    filter_list_files_nr = len(filter_list_files)
    print('\n Fund {} directories and {} files.'.format(str(filter_list_dir_nr),str(filter_list_files_nr)))

if __name__ == "__main__":
    sys.exit(main())
