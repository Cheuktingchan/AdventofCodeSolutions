
opener = open("polymer.txt","r")
polymers = opener.read()
polymeri = list(polymers)
alphabet = "abcdefghijklmnopqrstuvwxyz"
list_ = []

for e,let in enumerate(alphabet):
    polymer = list(filter(lambda a: a != let and a!= let.upper(),polymeri)) 
    t = 0
    for i in range(500):
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
    list_.append(len(polymer))
    
inde = list_.index(min(list_))
print(alphabet[inde])

file = open("ptwoletter.txt","w")
file.write(alphabet[inde])
