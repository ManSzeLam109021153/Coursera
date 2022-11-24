#使用 def 函式
def computepay(h, e):
    payment=(h*e)-(h-40)*e+((h-40)*e*1.5)
    return payment
h=float(input("Enter Hours:"))
e=float(input("Enter Hours Pay:"))    

if h <=40:
    print("Hours Pay:",h*e)
else:
    payment=computepay(h,e)
    print("Pay",payment)
    
