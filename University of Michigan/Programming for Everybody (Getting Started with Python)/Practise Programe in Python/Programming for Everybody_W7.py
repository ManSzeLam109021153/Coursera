largest = None
smallest = None
all_numbers = []
while True:
    num = input('Enter the Number:')
    if num == "done":
        break
    try:
        all_numbers.append(int(num))
    except:
        print('Invalid input')
        continue
#     else:
#         num=int(num)
largest = max(all_numbers)
smallest = min(all_numbers)
print("Maximum is", largest)
print("Minimum is", smallest)
