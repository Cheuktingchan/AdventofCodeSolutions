grid = [[0]*1000 for i in range(1000)]
    

elves = open("claims.txt","r")
elv = elves.read()
claims = elv.split("\n")

def get_cords_and_dims(claim):
    clem,clem,coord,dimen = claim.split()
    cordx,cordy = map(int,coord[:-1].split(","))
    wid,hei = map(int,dimen.split("x"))
    return cordx,cordy,wid,hei
for claim in claims:
    cordx,cordy,wid,hei = get_cords_and_dims(claim)
    for row in range(hei):
        for col in range(wid):
            grid[cordy + row][cordx + col] += 1

overlap = 0

for f in grid:
    for inch in f:
        if int(inch) >= 2:
            overlap += 1
print(overlap)
