import math

num =  int(input("Enter a Number:"))


def isperfectsquare(n):
    root = math.sqrt(n)
    if int (root + 0.5) ** 2 == n:
        print(f"{n} is a perfect square")
    else:
        print(f"{n} is not a perfect square")

isperfectsquare(num)