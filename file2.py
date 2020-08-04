# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s=0
l=0
ans=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    start = line.find("0")
    stringfloat=line[start:]
    #print(stringfloat)
    l=l+1
    fvalue=float(stringfloat)
    s=s + fvalue
    ans=s/l
    #print(line)
   
print("Average spam Confidence:",ans)
