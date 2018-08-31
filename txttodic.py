import json

def getdata(filename):

    members = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            dic = json.loads(line)
            members.append(dic)

    return members


if __name__ == '__main__':

    print(members[0]['fname'])
    for member in members:
        print(member)
    print(len(members))
