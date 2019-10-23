#!/usr/bin/env python3


import pwd
import os
import secrets
import string
import argparse

parser = argparse.ArgumentParser(description='Add users to system')
parser.add_argument('-f', '--file', required=True,
                    help='The file containing the users')
args = vars(parser.parse_args())

def username_exist(name):
    try:
        pwd.getpwnam(name)
    except KeyError:
        return False
    else:
        return True

def get_unique_username(name):
    username = name.replace(" ", "")
    while username_exist(username):
        username = username + "_"
    return username

def generate_random_password():
    letters = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(letters) for i in range(4))

def add_user_to_system(username):
    password = generate_random_password()
    # Add -k to copy standard files
    os.system("useradd -m -p "+password+" '"+username+"'")
    print(username+":"+password)


if __name__ == '__main__':
    with open(args["file"], encoding="ISO-8859-1") as fp:
        lines = fp.read().splitlines()
        for line in lines:
            add_user_to_system(get_unique_username(line))
