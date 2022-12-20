def numbertowords(n):
    first_twenty = ["", "One", "Two",
                    "Three", "Four", "Five",
                    "Six", "Seven", "Eight",
                    "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen",
                    "Fifteen", "Sixteen", "Seventeen",
                    "Eighteen", "Nineteen"]

    if (n<=0):
        print("Enter a positive number greater than 0")
    elif (n< 20):
        print(first_twenty[n])
    else:
        print("enter number between 1 and 20")

numbertowords(2)