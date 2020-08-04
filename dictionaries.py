name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dicts = dict()
#lst = list()
for line in handle:
    if not line.startswith("From:") : continue
    fromline = line.split()
    words=fromline[1]
    #lst.append(words)
     #print(words)
    
    dicts[words] = dicts.get(words,0)+1
print(dicts.items())        
bigword = None
bigcount = -1
for word,count in dicts.items() :
    if count<bigcount: continue
    bigword=word
    bigcount=count
    #print(word,count)
print(bigword,bigcount)        
