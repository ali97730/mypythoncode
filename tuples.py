name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dicts=dict()
for line in handle:
    if not line.startswith("From ") : continue
    fromline = line.split()
    #print(fromline)
    fulltime=fromline[5]
    #lst.append(words)
    hr=fulltime[:2]
    #print(fulltime)
    #print(hr)
    dicts[hr] = dicts.get(hr,0)+1
lst = list()
#print(dicts) 
for k,v in dicts.items():
    tup = (k,v)
    lst.append(tup)
lst = sorted(lst)

for k,v in lst:
    print(k,v)


