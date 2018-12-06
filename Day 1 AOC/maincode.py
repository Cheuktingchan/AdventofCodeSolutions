########### PART 1 ##############

nums = open("numbers.txt", "r")
n = nums.read()
nlist = n.split("\n")
anslist = list(map(int,nlist))
ans = sum(anslist)
print(ans)

######### PART 2 ################

ptwoans = 0
ptwoset = {0}

while True:
    for num in anslist:
        ptwoans += num
        if ptwoans in ptwoset:
            print(ptwoans)
            break
        ptwoset.add(ptwoans)
    else:
        continue
    break

    


