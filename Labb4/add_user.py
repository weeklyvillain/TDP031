import pwd
import os
import secrets
import string

def username_exist(name):
    try:
        pwd.getpwnam(name)
        return False
    except KeyError:
        return True

def get_unique_username(name):
    while username_exist(name):
        name = name + "_"
    return name

def generate_random_password():
    letters = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(letters) for i in range(10))

def add_user_to_system(username):
    password = generate_random_password()
    # Add -k to copy standard files
    os.system("sudo useradd -m -p "+password+" "+username)
    print(username+":"+password)


if __name__ == '__main__':
    # while read line:
        # uname = get_unique_username(line)
        # add_user_to_system(uname)
    # restart ypservice