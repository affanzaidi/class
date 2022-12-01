num1 = int(input("Enter the base number:"))
num2 = int(input("Enter the exponent number:"))

def exponential(n, m):
    result = 1
    for m in range(m, 0, -1):
        result *= n
    print(result)

exponential(num1, num2)
