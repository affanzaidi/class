num = int(input("Enter a number:"))


def bitcount(value):
    count= 0
    while(value):
        count += value & 1
        value >>= 1
    print(count)


bitcount(num)