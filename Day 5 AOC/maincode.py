opener = open("polymer.txt","r")
polymers = opener.read()
polymer = list(polymers)
print(polymer)
t = 0
while True:
    try:
        if polymer[t].isupper():
            if polymer[t + 1] == polymer[t].lower():
                polymer.pop(t)
                polymer.pop(int(t + 1))
                t = 0
                print(polymer)
            else:
                t += 1
        elif polymer[t].islower():
            if polymer[t + 1] == polymer[t].upper():
                  polymer.pop(t)
                  polymer.pop(int(t + 1))
                  t = 0
                  print(polymer)
                else:
                t += 1
    except IndexError:
        break

print(polymer)
