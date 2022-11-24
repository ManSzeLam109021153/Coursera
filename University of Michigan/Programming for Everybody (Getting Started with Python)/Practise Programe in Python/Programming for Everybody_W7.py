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

print("Maximum", max(num))
print("Min", min(num))