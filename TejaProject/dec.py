


def smart_div(func):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return func(x,y)
    return inner



@smart_div
def div1(a, b):
    print(a / b)

div1(2,4)