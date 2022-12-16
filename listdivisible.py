user_list = [10, 5, 17, 23, 6, 9]
number = input("Enter a number to divide: ")

for i in user_list:
    if i % int(number) == 0:
        print(f"{i} is divisible by {number}")
    else:
        print(f"{i} is not divisible by {number}")

