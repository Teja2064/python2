from numpy import *
arr1 = array([
               [1,24,3],
                [2,7,4],
                [34,5,67]

              ])
m1=matrix(arr1)
arr2= array([
    [1,2,4],
    [2,7,4],
    [3,6,7]
])
m2=matrix(arr2)
print(m1)
print(m2)
print(m1.ndim)
print(m2.ndim)
print(m1*m2)
