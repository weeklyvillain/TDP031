
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
    username = ''.join(c for c in name if c.isalnum())

    if len(username) == 0:
        username = generate_random_string(4)
    if len(username) > 15:
        username = username[:15]

    unique_username = username + generate_random_numbers(3)
    while username_exist(unique_username):
        unique_username = username + generate_random_numbers(3)
    return unique_username

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(secrets.choice(letters) for i in range(length))

def generate_random_numbers(length):
    numbers = string.digits
    return ''.join(secrets.choice(numbers) for i in range(length))

def generate_random_password():
    letters = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(letters) for i in range(4))

def clean_names(file, output):
    os.system("iconv -t ascii//TRANSLIT " + file + " -o " + output)

def add_user_to_system(username):
    password = generate_random_password()
    # Add -k to copy standard files
    os.system("useradd -m -p "+password+" '"+username+"'")
    os.system("echo {}:{} | chpasswd".format(username, password))
    print(username+":"+password)


if __name__ == '__main__':
    clean_names(args["file"], args["file"]+"_temp")
    with open(args["file"]+"_temp", encoding="ISO-8859-1") as fp:
        lines = fp.read().splitlines()
        for line in lines:
            add_user_to_system(get_unique_username(line))
    os.system("rm {}".format(args["file"]+"_temp"))
