n=int(input('enter the how much fib seq '))
x = int(input("enter the upto what number fib seq should stop"))
def fib(n):
    a=0
    b=1
    if n<=0:
        print("not defined")
    elif n==1:
        print(a)
    else:
        print("the fib seq is given below")
        print(a)
        print(b)

        for i in range(2,n):



            c=a+b
            a=b
            b=c

            if c<x:
                print(c)


fib(n)