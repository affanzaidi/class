num=int(input('Enter a number: '))
def fibonachi(n):
    a=0
    b=1
    count = 0
    if n<0:
        print("positive number only")
    elif n==0:
        print(a)
    elif n==1:
        print( b)
    else:
        while count < n:
            print(a)
            c=a+b
            a=b
            b=c
            count += 1


fibonachi(num)