from os import system, name

from time import sleep

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

def verifyed_grade():
    while True:
        tempgrade = input("\nEnter your Grade (FP or DP1 or DP2):\t").upper()
        if (tempgrade == 'FP' or tempgrade == 'DP1' or tempgrade == 'DP2'):
            return tempgrade
        else:
            print("Please enter the CORRECT Grade!")

def verifyed_email():
    while True:
        tempe = input("\nEnter your School Email:")
        if (tempe[-13:] == '@uwcchina.org'):
            return tempe
        else:
            print("Please enter the CORRECT School Email!")

c = CODE_with_UWC()

team_members = []

for i in range(20):

    c.mission()

    applicant = {}
    applicant['fname'] = input("\nEnter your first name:\t").lower()
    applicant['lname'] = input("\nEnter your last name:\t").lower()

    applicant['email'] = verifyed_email()
    applicant['grade'] = verifyed_grade()

    with open('members.txt', 'a') as f:

        f.write(str(applicant['fname'])+'\t')
        f.write(str(applicant['lname'])+'\t')
        f.write(str(applicant['grade'])+'\t')
        f.write(str(applicant['email'])+'\n')

    print("\nTHANK YOU!")

    team_members.append(applicant)

    sleep(2)

    system('clear')
