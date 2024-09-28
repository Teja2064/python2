from numpy import *
arr = array([1,2,3,4])
max_val = arr[0]
for i in arr[1:]:
    if i > max_val:
        max_val=i

print(max_val)
