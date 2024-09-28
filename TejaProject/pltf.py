
lst = [34,6,1,23,4,5,6,7,8,9,4,5]

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd




even,odd=count(lst)
print('even:{},odd:{}'.format(even,odd))
print(odd)
