import re
name = input("Enter file:")
if len(name) < 1 : name = "week1.txt"
lst=list()
handle = open(name)
for line in handle:
    line=line.rstrip()
    llst = re.findall("[0-9]+",line)
    for l in llst:
        lst.append(l)
print(lst)    
summation=0
for s in lst:
    summation=summation+int(s)
print(summation)