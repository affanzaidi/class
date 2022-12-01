num1 = int(input("Enter the base number:"))
num2 = int(input("Enter the exponent number:"))

def exponential(b , p):
    temp = num1
    for i in range(1,p+1):
        product = num1* temp
    print(product)



exponential(num1, num2)
