num =  int(input("Enter a Number:"))


def isperfectsquare(n):
    # root = math.sqrt(n)
    if int (n **(1/3)) ** 3 == n:
        print(f"{n} is a perfect cube")
    else:
        print(f"{n} is not a perfect cube")

isperfectsquare(num)