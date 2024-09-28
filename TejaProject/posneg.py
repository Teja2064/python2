x = int(input("enter  any number"))
y = int(input("enter any number"))
z = int(input("enter any number"))
if x > y and  x > z:
    print(" x is greater")
elif y > z and y > x :
    print(" y is greater")
elif z > x and z > y:
    print(" z is greater")
else:
    print(" wrong  output")
