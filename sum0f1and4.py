num = input(str("Enter a 4 digit number:"))

def sumof(value):
    if len(value) == 4:
        first_digit= int(value[0])
        last_digit = int(value[3])
        sum = first_digit +last_digit
        print((sum))
    else:
        print("Enter a 4 digit number only!")

sumof(num)