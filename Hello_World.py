from os import system, name
from time import sleep
import json
from txttodic import getdata
from verify import verifyed_email, verifyed_grade, verifyed_fname, verifyed_lname

class CODE_with_UWC(object):

    def __init__(self):
        self.C = "\n C = Connect to STEAM"
        self.O = "\n O = Open to the local community"
        self.D = "\n D = Design for peace, innovation and a sustainable future together"
        self.E = "\n E = Enpower GIRLS with code skills to explore boundless potential and passion in STEAM"

    def mission(self):
        print()
        string = "Welcome to CODE with UWC!"
        print(string.center(90))
        print(self.C)
        print(self.O)
        print(self.D)
        print(self.E)

def name_repetition(fname, lname, members, index):

    for i in range(index):
        if (fname == members[i]['fname'] and lname == members[i]['lname']):
            print("\nYou have already signed in!")

            clear()

            return True

    return False

def clear():

    sleep(1)

    system('clear')


if __name__ == '__main__':

    c = CODE_with_UWC()

    team_members = getdata('data.txt')

    i = len(team_members)
    while i <= 50:

        c.mission()

        applicant = {}
        applicant['fname'] = verifyed_fname()
        applicant['lname'] = verifyed_lname()

        if name_repetition(applicant['fname'], applicant['lname'], team_members, i):
            continue

        print('\n'+'\t %d people have already signed in.' %i)
        applicant['email'] = verifyed_email()
        applicant['grade'] = verifyed_grade()


        with open('members.txt', 'a') as f:

            f.write(str(applicant['fname'])+'\t')
            f.write(str(applicant['lname'])+'\t')
            f.write(str(applicant['grade'])+'\t')
            f.write(str(applicant['email'])+'\n')

        print("\nTHANK YOU!")

        with open('data.txt', 'a') as f:
            json.dump(applicant, f)
            f.write('\n')

        team_members.append(applicant)

        i += 1

        clear()
