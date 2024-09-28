number = 1

while number <= 500:
    square_root = int(number ** 0.5)
    if square_root * square_root == number:
        print(number)
    number += 1
