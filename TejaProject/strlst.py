#names=('tejesh',"rahjy",'mani','bhanu','jdgs','yurewi','gudyfiwy','navin','sai','swaroop')
x = int(input("give me how many  names you want"))
names=[]
if x>0:

    for i in range(x):
        n = input("give me the next name")
        i+=1
        names.append(n)
    def pount(names):
        for i in names:
            if len(i)>5:
                print(i)
    pount(names)




