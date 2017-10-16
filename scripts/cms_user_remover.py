from subprocess import call
import sys
import random
import hashlib


def parse_info(info):

    # this function must return an array of dictionary.
    # each element should have username which is added as a user
    # you may use same function used in 'cms_user_adder'

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

    if len(sys.argv) < 3:
        print("[*] Usage : python3 %s <user info file> <contest_id>" % sys.argv[0])
        exit()

    user_info_file = sys.argv[1]
    contest_id = sys.argv[2]

    users = open(user_info_file, 'r').readlines()
    user_info = parse_info(users)

    for info in user_info:
        # $ cmsRemoveParticipation <username> -c <contest_id>
        call(['cmsRemoveParticipation', info['username'],
            '-c', contest_id])

        # $ cmsRemoveUser <username>
        call(['cmsRemoveUser', info['username']])

    print('[+] Done removing user')

if __name__ == '__main__':
    main()
