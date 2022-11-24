# -*- coding: utf-8 -*-
user = input("Enter the Grade:")
try:
    user = float(user)
except:
    print("Error")
if user>=0.9:
    print("A")
elif user < 0.9 and user >=0.8:
    print("B")
elif user <0.8 and user >= 0.7:
    print("C")
elif user <0.7 and user >= 0.6:
    print("D")
else:
    print("F")