import re
import json
import hashlib
import getpass
from txttodic import getdata

class New_User(object):

    def __init__(self):
        self.username = None
        self.userpassport = None
        self.login = None
        self.score = None

    def create(self, members):
        self.username = verifyed_name(members, 'n')
        temppass = verifyed_newpass()
        self.userpassport = md5output(temppass)
        self.login = 1
        self.score = 0

    def printattr(self):
        print('\n'+'-'*10)
        print('\nUsername:'+str(self.username))
        print('\nlogin:\t'+str(self.login))
        print('\nscore:\t'+str(self.score))

class Old_user(New_User):
    def __init__(self, username, userpassport, login, score):
        self.username = username
        self.userpassport = userpassport
        self.login = login
        self.score = score

    def reward(self):
        self.login += 1
        self.score += 100

def json_output(members):
    with open('users.txt', 'r+') as f:
        for member in members:
            json.dump(member, f, default=lambda obj: obj.__dict__)
            f.write('\n')

def md5output(plaintext):
    md5 = hashlib.md5()
    md5.update(plaintext.encode('utf-8'))
    return md5.hexdigest()

def name_repetition(name, members, index):

    for i in range(index):

        if (name == members[i]['username']):
            print("\nUsername repeat!")
            flag = i

            return True, flag

    return False, None

def verified_password(md5):
    for i in range(5):
        temppass = getpass.getpass("\nEnter your password(%d):" %(5-i))
        if md5 == md5output(temppass):
            return True
        else:
            print("\nTry again!")
    return False

def verifyed_choice():
    while True:
        tempc = input("\nSign in (1) or Log in (2):\t")
        m = re.match(r'^(1|2)$', tempc)
        if m:
            return tempc

def verifyed_name(members, mode):
    while True:
        tempname = input("\nEnter your username(4-12 characters):\t")
        m = re.match(r'^\w{4,12}$', tempname)
        key, flag = name_repetition(tempname, members, len(members))

        if m:
            if mode == 'n' and not key:
                return tempname
            elif mode == 'o' and key:
                return flag
            else:
                print('\nMust be between 4-12 characters!')

def verifyed_newpass():
    while True:
        temppass = input("\nEnter your password(8-12 characters):\t")
        m = re.match(r'^\w{8,12}$', temppass)
        if m:
            return temppass
        else:
            print('\nMust be between 8-12 characters!')

def dic2user(dic):
    return Old_user(dic['username'], dic['userpassport'], dic['login'], dic['score'])

def user2dic(user):
    return {'username':user.username, 'userpassport':user.userpassport, 'login':user.login, 'score':user.score}

if __name__ == '__main__':

    members = getdata('users.txt')

    print("\nWelcome to the Oasis")
    choice = verifyed_choice()

    tempuser = New_User()

    if (choice == '1'):
        tempuser.create(members)
        members.append(user2dic(tempuser))
        json_output(members)
        tempuser.printattr()
    else:
        flag = verifyed_name(members, 'o')
        if not verified_password(members[flag]['userpassport']):
            print('Go away!')
        else:
            tempuser = dic2user(members[flag])
            tempuser.reward()
            members[flag] = user2dic(tempuser)
            json_output(members)
            tempuser.printattr()
