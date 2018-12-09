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
        dic[str(infos[i][:-12].split("#")[1])].append(-int(time[i + 1]))
        dic[str(infos[i][:-12].split("#")[1])].append(int(time[i + 2])) 
        dicdiff[str(infos[i][:-12].split("#")[1])] = sum(dic[str(infos[i][:-12].split("#")[1])]) 
print(dicdiff) # guard 73 sleeps the most

                    

    
        
        
        
