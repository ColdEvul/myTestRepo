#!/usr/bin/env python3

# Requires pygit2 (pip install pygit2)
import sys
import configparser
import pygit2

config = configparser.ConfigParser()
config.sections()

def getConfig():
    exist = config.read('deploy.ini')
    if exist != '':
        return True
    else:
        return False


def getContent():
    return content

def main():
    # Check for config
    if not getConfig():
        sys.exit("No config is found")
    repo = config.get('GIT', 'repo', fallback='')
    head = repo.lookup_reference('HEAD').resolve()
    head = repo.head
    print(head)

if __name__ == "__main__":
    sys.exit(main())
