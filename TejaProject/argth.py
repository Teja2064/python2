#position

def person(tiger,**b):
    print(tiger)
    for y,k in b.items():
        print(y,k)

person('sunderbands',name='teja', age = 24, mob=3852,weight=65,country ='us')