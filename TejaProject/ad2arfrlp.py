from numpy import *
a = array([1,2,4,6])
y = array([3,4,5,6])
result=[]
for e in range(len(a)):
    h = array(a[e]+y[e])
    result.append(h)
output=array(result)
print(output)

