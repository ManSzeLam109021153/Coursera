largest = None
smallest = None
while True:
    num = input('Enter the Number:')
    if num == "done":
        break
    try:
        user=int(num)
    except:
        print('Invalid input')
        continue
    else:
        num=int(num)
largest = max(num)
smallest = min(num)
print("Maximum is", largest)
print("Minimum is", smallest)
