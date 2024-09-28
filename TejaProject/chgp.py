x = int(input("Enter the number of names you want: "))
names = []

if x > 0:
    for i in range(x):
        name = input("Enter name {}:".format(i+1))
        names.append(name)

def print_names(names):
    for name in names:
        if len(name) > 5:
            print(name)




print("Names with more than 5 letters:")
print_names(names)

