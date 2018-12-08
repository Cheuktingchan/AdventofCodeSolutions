grid = {}
for i in range(1000):
    grid[str(i)] = []
    for it in range(1000):
        grid.setdefault(str(it),[]).append(0)

elves = open("claims.txt","r")
elv = elves.read()
claims = elv.split("\n")

claimno = []
coords = []
size = []

for i in claims:
    claimno.append(i.split("@")[0])
print(claimno)
            
    
