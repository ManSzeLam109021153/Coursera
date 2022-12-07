fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("No such file exist")
    quit()
count = 0
total = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        pos = line.find(" ")
        #print (pos)
        new_line = line[pos:]
        new_line.strip() 
        count = count +1
        total = total + float(new_line)
average = total/count
print("Average spam confidence:",average)