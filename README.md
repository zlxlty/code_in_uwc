![code with uwc](code_with_uwc)

### This is a program for my girlfriend's `Code with UWC` zhixing fair.  

***
## Content
* [Environment](#environment)
* [Instruction](#instruction)
    * Basic Function
    * Special Feature
    * Reminder
* [Hello_World](#hello_world)
* [verify](#verify)
* [txttodic](#txttodic)

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
## Hello_World
`Hello_World.py` program is used for registering people who are interested to join this zhixing.  
I will explain `classes` and `functions` in this file respectively
```python
class CODE_with_UWC(object):
    def __init__(self):
        pass
    def mission(self):
        pass
```
The only application of this `class` is to print the mission of this zhixing

```python
def name_repetition(fname, lname, members, index):
    pass
```
This function will check wether the name input is in `memebers.txt` already  
if the name dose repeat, the function will return **`TRUE`**, otherwise it will return **`FALSE`**

```python
def clear():
    pass
```
Once a student finish all the inputs, this function will be used to clear the terminal  
All the information will be temporarily stored in a `list` of `dictionary`. Then, those `dictionary` will be `serialize` by `json` and stored in `data.txt`

***
## verify
`verify.py` includes many functions that are used to validate user's input such as `first name`, `last name`, `email` and `grade`.

```python
def verifyed_fname():
    pass
def verifyed_lname():
    pass
```
Those two functions will return verified names if the input is not `''` or `'\n'`

```python
def verifyed_email():
    pass
```
This function only return valid email address if and only if the address end with `uwcchina.org` and they year number is in `16`, `17`, `18`  
```python
m = re.match(r'^\w+?(\d{2})@uwcchina\.org$', email)
```
`Regular Expressions` is used to comparing the formal with the input

```python
def verifyed_grade():
    pass
```
It will only return one of the valid grades in UWCCSC

##txttodic
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
This function can transform serialized content in `data.txt` to a list of dictionaries

***
The results will be recorded in `members.txt` so that my girlfriend can make an Excel sheet out of it conveniently  

****

|Author|SkyL|
|---|---
|E-mail|2924312854@qq.com


****
