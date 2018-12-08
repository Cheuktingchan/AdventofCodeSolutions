###############PART 1#############################

grid = [[0]*1000 for i in range(1000)]

elves = open("claims.txt","r")
elv = elves.read()
claims = elv.split("\n")

for claim in claims:
    clem,clem,coord,dimen = claim.split()
    cordx,cordy = map(int,coord[:-1].split(","))
    wid,hei = map(int,dimen.split("x"))
    for row in range(hei):
        for col in range(wid):
            grid[cordy + row][cordx + col] += 1

overlap = 0

for f in grid:
    for inch in f:
        if int(inch) >= 2:
            overlap += 1
            
print(overlap)

########################PART 2 ######################

for claim in claims:
    clem,clem,coord,dimen = claim.split()
    cordx,cordy = map(int,coord[:-1].split(","))
    wid,hei = map(int,dimen.split("x"))
    checker = []
    for row in range(hei):
        for col in range(wid):
            grid[cordy + row][cordx + col] += 1
            checker.append(grid[cordy + row][cordx + col])
    if all(elem == 2 for elem in checker):
        print(cordx,cordy)
            
