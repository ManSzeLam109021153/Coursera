hrs = input("Enter Hours:")
h = float(hrs)
ehrs=input("Enter each pay:")
e = float(ehrs)
if h <40:
    print(e*h)
else:
    print((h*e)-(h-40)*e+((h-40)*e*1.5))
    '''(h*e)-(h-40)*e+((h-40)*e*1.5) = (45 X 10.5) - (45 - 40) X 10.5 + [(45 - 40) X 10.5 X 1.5]'''
