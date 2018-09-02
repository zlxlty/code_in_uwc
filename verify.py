# r'^\s+(\w+?)(\d{2})@(\w{8}).(\w{3})$'
import re

def verifyed_email():

    while True:
        email = input("\nEnter Your Email:\t").strip()
        m = re.match(r'^(\w+?)(\d{2})@(\w{8})\.(\w{3})$', email)

        if m:
            if m.group(3) != 'uwcchina' or m.group(4) != 'org':
                print("\nPlease Enter the CORRECT school Email!")

            elif not m.group(2) in ['16','17','18']:
                print("\nEmail expired!")

            else:
                return email
        else:
            print("\nPlease Enter the CORRECT school Email!")

def verifyed_grade():
    while True:
        tempgrade = input("\nEnter your Grade (FP or DP1 or DP2):\t").upper()
        if (tempgrade == 'FP' or tempgrade == 'DP1' or tempgrade == 'DP2'):
            return tempgrade
        else:
            print("Please enter the CORRECT Grade!")

def name_repetition(fname, lname, members, index):

    for i in range(index):
        if (fname == members[i]['fname'] and lname == members[i]['lname']):
            print("\nYou have already signed in!")

            clear()

            return True

    return False

def verifyed_fname():
    while True:
        tempn = input("\nEnter your first name:\t").lower()
        if not tempn in ["", "\n"]:
            return tempn

def verifyed_lname():
    while True:
        tempn = input("\nEnter your last name:\t").lower()
        if not tempn in ["", "\n"]:
            return tempn


if __name__ == '__main__':
    email = verifyed_email()
