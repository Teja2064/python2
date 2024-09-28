a=435
print(id(a))
def crec():

    a=56
    print(id(a))
    x=globals()['a']
    print(id(x))
    print('in fun',a)
    globals()['a']=23
crec()

print(a)