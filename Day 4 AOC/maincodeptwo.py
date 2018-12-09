open_ = open("guardlog.txt","r")
read = open_.read()
log = read.split("\n")
log = sorted(log)

time = []
info =[]
for a in log:
    time.append(a.split()[1])
    info.append(a.split("]")[1])
    
times = []
for b in time:
    times.append(b[:-1])

time = []
for r,v in enumerate(times):
    time.append(times[r].split(":")[1])
    
infos = []
for d in info:
    infos.append(d[1:])

dic = {}
dicdiff = {}

for i,e in enumerate(log):
    if infos[i][0] == "G":
        dic[str(infos[i][:-12].split("#")[1])] = []
        for u in range(60):
            dic[str(infos[i][:-12].split("#")[1])].append(0)
        
for i,e in enumerate(log):
    if infos[i][0] == "G":
        t = dic[str(infos[i][:-12].split("#")[1])]
    if infos[i][0] == "f":
        f = int(time[i])
    if infos[i][0] == "w":
        w = int(time[i])
        for x in range(f,w):
            t[x] += 1

for i,e in enumerate(log):
    if infos[i][0] == "G":
        dicdiff[str(infos[i][:-12].split("#")[1])] = sum(dic[str(infos[i][:-12].split("#")[1])])
dicv = dic.values()
dick = list(dic.keys())
for i in dicv:
    print(max(i) ) #guard with highest minute slept is the 17th one
print(dick[17]) #17th one is guard 191

print(dic["191 "]) # minute 26 is the one guard 191 slept the most

print(26 * 191)
