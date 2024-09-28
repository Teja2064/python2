from functools import *
nums =[3,4,5,10,11]
a=list(filter(lambda i:i>=5,nums))
print(a)
b=list(map(lambda n:n-2,nums))
print(b)
c=reduce(lambda d,c:d*c,a)
print(c)

