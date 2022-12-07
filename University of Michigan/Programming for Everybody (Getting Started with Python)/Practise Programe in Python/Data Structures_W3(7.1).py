# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for a in fh:
    b=a.rstrip()
    print(b.upper())