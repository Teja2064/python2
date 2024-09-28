available = int(input("total stock"))
p = int(input("how many candies you want?"))

for i in range(p):
    if available>0:
        print("candies")
        available-=1
    else:
        print("out of stock")
        break




print("bye")