import itertools
grid = {}
for i in range(1000):
    grid[str(i)] = []
    for it in range(1001):
        grid.setdefault(str(it),[]).append(0)

elves = open("claims.txt","r")
elv = elves.read()
claims = elv.split("\n")

claimno = []
coords = []
size = []

for i in claims:
    claimno.append(i.split("@")[0])
    coords.append(i.split(" ")[2])
    size.append(i.split(" ")[3])

claimnor = []
for claimn in claimno:
    claimnor.append(claimn[1:])
claimno = list(map(int,claimnor))

chordx = []
coordy = []

for coord in coords:
    chordx.append(coord.split(",")[0])
    coordy.append(coord.split(",")[1])
    
chordy = []

for cody in coordy:
    chordy.append(cody.split(":")[0])
coordy = list(map(int,chordy))
coordx = list(map(int,chordx))

sizex = [] 
sizey = []
for sides in size:
    sizex.append(sides.split("x")[0])
    sizey.append(sides.split("x")[1])

sidex = list(map(int,sizex))
sidey = list(map(int,sizey))
    
for i,cordy in enumerate(coordy):
    cordx = coordx[i]
    sizex = sidex[i]
    sizey = sidey[i]
    for a in range(sizex):
        for b in range(sizey):
            try:
                grid[str(cordy + b)][cordx + a] += 1
            except IndexError:
                continue

allnums = list(grid.values())
flat = itertools.chain.from_iterable(allnums)

overlap = 0
for a in flat:
    if a > 1:
        overlap += 1
print(overlap)
