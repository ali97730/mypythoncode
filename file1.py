# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)



for t in fh:
    t=t.rstrip()
    t=t.upper()
    print(t)
    


