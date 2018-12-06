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
