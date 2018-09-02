# r'^\s+(\w+?)(\d{2})@(\w{8}).(\w{3})$'
import re

def verifyed_email():

    while True:
        email = input("\nEnter your Email:\t").strip()
        m = re.match(r'^\w+?(\d{2})@uwcchina\.org$', email)

        if m:

            if not m.group(1) in ['16','17','18']:
                print("\nEmail expired!")

            else:
                return m
        else:
            print("\nPlease Enter the CORRECT school Email!")

def verifyed_grade():
    while True:
        tempgrade = input("\nEnter your Grade (FP or DP1 or DP2):\t").upper().strip()
        if (tempgrade == 'FP' or tempgrade == 'DP1' or tempgrade == 'DP2'):
            return tempgrade
        else:
            print("Please enter the CORRECT Grade!")


def verifyed_fname():
    while True:
        tempn = input("\nEnter your first name:\t").lower().strip()
        if not tempn in ["", "\n"]:
            return tempn

def verifyed_lname():
    while True:
        tempn = input("\nEnter your last name:\t").lower()
        if not tempn in ["", "\n"]:
            return tempn


if __name__ == '__main__':
    email = verifyed_email()
