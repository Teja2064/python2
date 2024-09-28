
p=1
def fact(m):
    global p
    for i in range(1,m+1):
        p=p*i
    return p



x=5
fact(x)
print(p)