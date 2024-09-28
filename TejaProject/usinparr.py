from array import *
arr=array('i',[])
k=int(input("enter the lenght of array you want"))
for x in range(k):
    c=int(input("enter the value"))
    arr.append(c)
print(arr)
values= int(input("enter the element you want to search"))
t=0
for e in arr:
    if e==values:
        print(t)
        break
    t+=1
print(arr.index(values))