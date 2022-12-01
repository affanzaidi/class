num = int(input("Enter your number: "))
close_to = int(input("Round off to: "))

def roundoff(num, round_off_to):
    mod = num % round_off_to
    if num < round_off_to:
        print(round_off_to)
    elif (num%round_off_to) < (round_off_to/2):
        print(num-mod)
    else :
        print(num + (round_off_to-mod))

roundoff(num, close_to)

