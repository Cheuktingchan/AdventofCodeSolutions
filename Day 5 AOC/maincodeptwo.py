opener = open("polymer.txt","r")
polymers = opener.read()
alphabet = "abcdefghijklmnopqrstuvwxyz"

dic = {}
for a in alphabet:
    dic[a] = list(filter(lambda x: x != a.lower() and x != a.upper() , polymers))

def reactor(x,y):
    if y.isupper():
        if x == y.lower():
            return True
    elif y.islower():
        if x == y.upper():
            return True
    else:
            return False

list_ = []
nearlyans = []
for a in alphabet:
    for p in dic[a]:
        try:
            if list_ and reactor(p,list_[-1]):
                list_.pop(-1)
            else:
                list_.append(p)
        except IndexError:
            continue
    nearlyans.append(len(list_))
    list_ = []

print(min(nearlyans))
    
