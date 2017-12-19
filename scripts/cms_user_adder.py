from subprocess import call
import sys
import random
import hashlib


def parse_info(info):

    # this function must return an array of dictionary.
    # each element should have username, password, first_name, last_name

    '''

    # PARSING SAMPLE
    # YOU SHOULD IMPLEMNET THIS BY USERSELF

    data = []
    cnt = 1
    for row in info:
        r = row.strip().split()
        pw = hashlib.md5(str(random.random()).encode()).hexdigest()

        d = {
            'username': r[0],
            'password': pw,
            'first_name': r[1],
            'last_name': r[2],
        }

        data.append(d)
        cnt += 1

    return data

    '''

    return [
        {
            'username': 'iam',
            'password': 'mr',
            'first_name': 'Donald',
            'last_name': 'Trump',
        }
    ]


def main():

    if len(sys.argv) < 2:
        print("[*] Usage : python %s <user info file>" % sys.argv[0])
        exit()

    user_info_file = sys.argv[1]

    users = open(user_info_file, 'r').readlines()
    user_info = parse_info(users)

    login_info = ['Username,Password']

    for info in user_info:

        # $ cmsAddUser <first name> <last name> <username> -p <password>
        call(['cmsAddUser', info['first_name'], info['last_name'], info['username'],
              '-p', info['password']])

        # user login info
        login_info.append('%s,%s' % (info['username'], info['password']))

    # saves user login info in csv format
    login_info_file = 'login_info.csv'
    with open(login_info_file, 'w') as f:
        for info in login_info:
            f.write(info + '\n')

    print('[+] Done Adding user, file saved')

if __name__ == '__main__':
    main()
