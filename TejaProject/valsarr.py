from array import *
vals = array('i',[3,2,1,-2,5])

NewaArr = array(vals.typecode,(a for a in vals))

i = 0
while i<len(NewaArr):
    print(NewaArr[i])
    i+=1

NewaArr.sort()
print(NewaArr)
