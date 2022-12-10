#Use mbox-short.txt as the file name
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails = {}
for line in handle:
    if "From:" in line: continue
    elif "From" in line:
        line = line.split("From")
        line = (str(line[1]).strip()).split( )
        if line[0] not in emails.keys():
            emails[line[0]] = 1
        else:
            emails[line[0]] = emails.get(line[0],0) + 1        
    else: continue
freq = [(value,key) for key,value in emails.items()]
print(max(freq)[1],max(freq)[0])
