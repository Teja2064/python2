num=int(input("give any number"))

if num==0 or num==1:
    print("is not prime")

for i in range(2,num):
    if num%i==0:
        print(num,"is not prime")
        break
    else:
        print(num,"is prime")

print("bye")