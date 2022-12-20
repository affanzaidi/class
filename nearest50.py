num = input(("Enter a number to round off :"))

def roundoff(value):
    last2 = value[-2:]
    if int(last2) > 25:
        print(value[:-2]+"50")
    else:
        print(value[:-2]+"00")
    print(last2)

roundoff(num)