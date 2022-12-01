num1 = int(input("Enter the number:"))
num2 = int(input("Enter the second number:"))

def is_divisible(num1, num2):
    if (num1 % num2 == 0):
        print(f"{num1} is divisible by {num2}")
    else :
        print(f"{num1} is not divisible by {num2}")

is_divisible(num1, num2)
