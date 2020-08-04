fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"#if user dont give any file name

fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    if not line.startswith("From:") : continue
    words = line.split()
    #print(words)
    email = words[1]
    count = count +1
    print(email)   
 
    #print(line)
   
print("There were", count, "lines in the file with From as the first word")
