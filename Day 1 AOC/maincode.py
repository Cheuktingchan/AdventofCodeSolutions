########### PART 1 ##############

nums = open("numbers.txt", "r")
n = nums.read()
nlist = n.split("\n")
anslist = list(map(int,nlist))
ans = sum(anslist)
print(ans)

######### PART 2 ################

ptwodic = {}
ptwodic["0"] = anslist[0]
for i in range(len(anslist)):
    if i == 0:
        pass
    else:
        ptwodic[str(i)] = ptwodic[str(i-1)] + anslist[i]

ptwolist = list(ptwodic.values())

ptwoset = set()

for i in range(len(ptwolist)):
    if int(ptwolist[i]) in ptwoset:
        print(ptwolist[i])
    elif not ptwolist[i] in ptwoset:
        ptwoset.add(int(ptwolist[i]))
    


