from collections import Counter

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
dicwholediff = {}
for i,e in enumerate(log):
    if infos[i][0] == "G":
        dic[str(infos[i][:-12].split("#")[1])] = []
        dicdiff[str(infos[i][:-12].split("#")[1])] = []
        
        
for i,e in enumerate(log):
    if infos[i][0] == "G":
        dic[str(infos[i][:-12].split("#")[1])].append(int(time[i + 1]))
        dic[str(infos[i][:-12].split("#")[1])].append(int(time[i + 2])) 
        dicdiff[str(infos[i][:-12].split("#")[1])] = sum(dic[str(infos[i][:-12].split("#")[1])])
 # guard 73 sleeps the most found by using the code above but with negative even indices and then suming the odd and even
mins = []
for i in range(60):
    mins.append(0)
for i,e in enumerate(log):
    try:
        for x in range(int(time[i + 1]),int(time[i + 2])):
            mins[x] += 1
    except IndexError:
        continue
print(mins) ]   
    
print(dic["73 "])



data = Counter(dic["73 "])
print(data.most_common())
print(data.most_common(1))



                    

    
        
        
        
