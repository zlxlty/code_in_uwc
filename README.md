CODE_with_UWC
===========================

This is a program for my girlfriend's `Code with UWC` zhixing fair.  

***
##Content
* [Environment](#Environment)
* [Instruction](#Instruction)
    * Basic Function
    * Special Feature
    * Reminder
* [Hello_World.py](#Hello_World.py)
* [verify.py](#verify.py)
* [txttodic.py](#txttodic.py)

***
### Environment
* python 3.6.5
* conda 4.5.4
If you haven't install anaconda on your computer, here is the URL link to [Download Anaconda](https://www.anaconda.com/download)

***
### Instruction
The **Main Function** of this program is [Hello_World.py](#Hello_World.py). Run this python program in the terminal using:
    $ python Hello_World.py







The `Hello_World.py` program is used for registering people who are interested to join this zhixing.  
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
