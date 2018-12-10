opener = open("polymer.txt","r")
polymers = opener.read()
polymer = list(polymers)
alphabet = "abcdefghijklmnopqrstuvwxyz"


for let in alphabet:
    polymer = list(filter(lambda a: a != let and a!= let.upper(),polymer)) 
    t = 0
    for i in range(50):
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
