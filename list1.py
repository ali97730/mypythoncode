fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()# here i have whole line
    words = line.split()
    #print(words)# whole line splitted into words['But', 'soft', 'what', 'light', 'through', 'yonder', 'window', 'breaks']
    for i in range(len(words)): #
        temp = words[i]
        #print(temp)
        if temp not in lst:
            #print("hello")
            lst.append(words[i])

lst.sort()
print(lst)            
        
