![code with uwc](code_with_uwc)

### This is a program for my girlfriend's `Code with UWC` zhixing fair.  

***
## Content
* [Environment](#Environment)
* [Instruction](#Instruction)
    * Basic Function
    * Special Feature
    * Reminder
* [Hello_World.py](#Hello_World.py)
* [verify.py](#verify.py)
* [txttodic.py](#txttodic.py)

***
## Environment
* python 3.6.5
* conda 4.5.4  
If you haven't install anaconda on your computer, here is the URL link to [Download Anaconda](https://www.anaconda.com/download)

***
## Instruction
### Basic Function
The **Main Function** of this program is [Hello_World.py](#Hello_World.py).  
Run this python program in the terminal using:
```
$ python Hello_World.py
```
Then following output should be seen on your terminal
```
                             Welcome to CODE with UWC!                                 

 C = Connect to STEAM

 O = Open to the local community

 D = Design for peace, innovation and a sustainable future together

 E = Enpower GIRLS with code skills to explore boundless potential and passion in STEAM
```
This is an explanation of the main values in this zhixing using initials of `CODE`

The program will then ask students to fill in their **name**, **Email** and **grade** for registration.  
Here is an example:
```
Enter your first name:	tianyi

Enter your last name:	lu

	 0 people have already signed in.

Enter your Email:	tylu17@uwcchina.org

Enter your Grade (FP or DP1 or DP2):	dp1

THANK YOU!
```

***
### Special Feature
* **SPACE** `''` will be identified as invalid input
```
Enter your first name:

Enter your first name:

Enter your first name:

Enter your first name:

Enter your first name:

Enter your first name:
```
* Name repetition can be detected by comparing with names in `data.txt`
```
Enter your first name:	tianyi

Enter your last name:	lu

You have already signed in!
```
* Only **UWC School Email** that end with `uwcchina.org` can be accepted
```
Enter your Email:	2924312854@qq.com

Please Enter the CORRECT school Email!
```
* **Expired** school email is invalid
```
Enter your Email:	tylu15@uwcchina.org

Email expired!
```
* Grade other than `FP`, `DP1` or `DP2` is invalid
```
Enter your Grade (FP or DP1 or DP2):	dp4

Please enter the CORRECT Grade!
```

***
### Reminder
* For students who are not familiar with terminal operation, please remind them to press `Enter` every time they finish typing.
* The number of students in `data.txt` and `members.txt` must be the same.

***
## Hello_World.py
`Hello_World.py` program is used for registering people who are interested to join this zhixing.  
I will explain `classes` and `functions` in this file respectively
```python
class CODE_with_UWC(object):
    def __init__(self):
        skip()
    def mission(self):
        skip()
```
The only application of this `class` is to print the mission of this zhixing

```python
def name_repetition(fname, lname, members, index):
    skip()
```
This function will check wether the name input is in `memebers.txt` already  
if the name dose repeat, the function will return **`TRUE`**, otherwise it will return **`FALSE`**

```python
def clear():
    skip()
```
Once a student finish all the inputs, this function will be used to clear the terminal


The results will be recorded in `members.txt` so that she can make an Excel sheet out of it conveniently  
The json output will be stored in `data.txt` and used as an input for `team_members`

```Python
#from txttodic.py import getdata
team_members = getdata('data.txt')
```

```Python
import json

def getdata(filename):

    members = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            dic = json.loads(line)
            members.append(dic)

    return members
```

****

|Author|SkyL|
|---|---
|E-mail|2924312854@qq.com


****
