import json

class CODE_with_UWC(object):

    def __init__(self):
        self.C = "\n C = Connect to STEAM"
        self.O = "\n O = Open to the local community"
        self.D = "\n D = Design for peace, innovation and a sustainable future together"
        self.E = "\n E = Enpower GIRLS with code skills to explore boundless potential and passion in STEAM"

    def mission(self):
        print(self.C)
        print(self.O)
        print(self.D)
        print(self.E)

class Participant(object):

    def __init__(self):
        self.key = False

    @property
    def person(self):
        return self.person

    @person.setter
    def person(self, gender):

        if not gender.upper() == "FEMALE":
            print("\nReally sorry, this zhixing is currently for girls only.")

        else:
            print("\nWelcome!")
            self.key = True


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
c.mission()

team_members = []

for i in range(20):

    applicant = {}
    applicant['fname'] = input("\nEnter your first name:\t").lower()
    applicant['lname'] = input("\nEnter your last name:\t").lower()
    applicant['gender'] = input("\nenter your gender:\t")

    p = Participant()
    p.person = applicant['gender']

    if not p.key:
        continue

    applicant['email'] = verifyed_email()
    applicant['grade'] = verifyed_grade()

    with open('members.txt', 'a') as f:

        f.write(str(applicant['fname'])+'\t')
        f.write(str(applicant['lname'])+'\t')
        f.write(str(applicant['grade'])+'\t')
        f.write(str(applicant['email'])+'\n')

    print("\nTHANK YOU!")

    team_members.append(applicant)

for member in team_members:
    print(member)
