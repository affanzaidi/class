operation = input("Enter the operation (ex: +, -, *, /): ")

operand1 = int(input("Enter the first operand: "))
operand2 = int(input("Enter the second operand: "))

if operation == "+":
    result = operand1 + operand2
    print(f"{operand1} + {operand2} = {result}")
elif operation == "-":
    result = operand1 - operand2
    print(f"{operand1} - {operand2} = {result}")
elif operation == "*":
    result = operand1 * operand2
    print(f"{operand1} * {operand2} = {result}")
elif operation == "/":
    result = operand1 / operand2
    print(f"{operand1} / {operand2} = {result}")
else:
    print("Invalid operation")