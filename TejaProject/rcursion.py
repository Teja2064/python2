import sys

print(sys.getrecursionlimit())
i=0
def rescur():
    global i
    i+=1
    print('teja',i)
    rescur()
rescur()