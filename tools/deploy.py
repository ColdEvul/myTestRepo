#!/usr/bin/env python3
import sys
import os
import configparser
import git
import shutil

# check argumetns
arguments = sys.argv

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


def main():
    # Info
    print('MD4 Deploy')
    print('This is a automated deploy script written for MD4 a Hearts of Iron 4 modification.')
    print('Written by: Andreas Brostrom | Evul <andreas.brostrom.ce@gmail.com>\n')

    # info if test build is made
    if 'testbuild' in arguments:
        print (" Note: Release folder will be removed after build is compleeted...\n")

    # Check for config
    checkConfig = os.path.isfile('tools\\deploy.ini')
    if checkConfig:
        config.read('tools\\deploy.ini')
    else:
        sys.exit("Could not find config file...")

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
    for root, dirs, files in os.walk(root_path, topdown=True):
        dirs[:] = [d for d in dirs if d not in blacklist_list]
        files[:] = [f for f in files if f not in blacklist_list]
        filter_list_dir.append(dirs)
        filter_list_files.append(files)
    countDir = len(filter_list_dir)
    countFiles = len(filter_list_files)
    print('\n Found a total of {} directories and {} files.\n'.format(str(countDir),str(countFiles)))

    # Continue?
    #input('Press enter to continue...')

    # Preping build
    # Creating release folder
    if not os.path.exists('release'):
        print('No release folder found creating folder...')
        os.makedirs('release')

    MOD = config.get('COMMON', 'ModName')
    if not os.path.exists('release\\{}'.format(MOD)):
        print('Prepering release build...')
        os.makedirs('release\\{}'.format(MOD))

    # Creating release directoys and files
    print('Building folder structure...')
    releaseFolder = '{}\\release\\{}'.format(root_path,MOD)
    os.chdir(releaseFolder)

    for dirs in filter_list_dir:
        dirList = []
        for dir in dirs:
            dirList.append(dir)
            try:
                os.makedirs('\\'.join(dirList))
                print('Setting up folder: {}\\{}'.format(MOD,'\\'.join(dirList)))
            except:
                sys.exit('Release folder is not empty. Pleace clean and rerun...')


    # subDir = []
    # for dirs in filter_list_dir:
    #     for dir in dirs:
    #         if len(dirs) <= 1:
    #             os.makedirs('\\{}'.format(MOD,dir))
    #         else:
    #             subDir.append('\\{}'.format(dir))
    #             subDir = ''.join(subDir)
    #             os.makedirs('{}\\'.format(MOD,subDir))
        #shutil.copy2(dirs, releaseFolder)

    if 'testbuild' in arguments:
        os.chdir(root_path)
        print(root_path)
        shutil.rmtree('\\release', ignore_errors=True)

if __name__ == "__main__":
    sys.exit(main())
