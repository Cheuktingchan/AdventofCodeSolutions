opener = open("daysix.txt","r")
reader = opener.read()
puzle =  reader.split()
newpuzzle = []
for i in puzle:
    newpuzzle.append(int(i))
seen = []
seen.append(newpuzzle)
counter = 0
boolean = True
for e in range(1000000000000):
    newpuzzle = newpuzzle.copy()
    maxi = newpuzzle.index(max(newpuzzle))
    oldmax = int(max(newpuzzle))
    newpuzzle[maxi] = 0
    incrementer = maxi
    counter += 1
    for i in range(oldmax):
        if incrementer > int(len(newpuzzle) - 2):
            incrementer = -1
            newpuzzle[int(incrementer + 1)] += 1
            incrementer += 1
        else:
            newpuzzle[int(incrementer + 1)] += 1
            incrementer += 1
    if newpuzzle in seen:
        break
    seen.append(newpuzzle)

print(counter)




