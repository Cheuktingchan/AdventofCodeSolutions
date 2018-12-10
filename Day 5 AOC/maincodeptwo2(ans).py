opener1 = open("ptwoletter.txt","r")
ptwoletter = opener1.read()
opener = open("polymer.txt","r")
polymers = opener.read()
polymeri = list(polymers)
alphabet = "abcdefghijklmnopqrstuvwxyz"
list_ = []


polymer = list(filter(lambda a: a != ptwoletter and a!= ptwoletter.upper(),polymeri))
t = 0
for i in range(500000000):
    try:
        if polymer[t].isupper():
            if polymer[t + 1] == polymer[t].lower():
                polymer.pop(t)
                polymer.pop(t)
                t = 0
            else:
                t += 1
        elif polymer[t].islower():
            if polymer[t + 1] == polymer[t].upper():
                  polymer.pop(t)
                  polymer.pop(t)
                  t = 0
            else:
                t += 1
    except IndexError:
        pass
print(len(polymer))
