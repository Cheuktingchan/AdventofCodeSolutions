#########PART 1##########################

boxids = open("boxids.txt","r")
b = boxids.read()
boxes = b.split("\n")
letters = "abcdefghijklmnopqrstuvwxyz"

twotimes = {}
threetimes = {}
counttwo = 0
countthree = 0

for boxid in boxes:
    for lets in letters:
        lettercount = boxid.count(lets)

        if lettercount == 2:
            twotimes[str(boxid)] = lets
        elif lettercount == 3:
            threetimes[str(boxid)] = lets

print(len(twotimes)*len(threetimes))

#############PART 2#######################

for i,boxid1 in enumerate(boxes):
    for boxid2 in boxes[i + 1:]:
        letsdiff = 0
        for a,char in enumerate(boxid1):
            char2 = boxid2[a]
            if char != char2:
                letsdiff += 1
        if letsdiff == 1:
            print(boxid1,boxid2)
            break
