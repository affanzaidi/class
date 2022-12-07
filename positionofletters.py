letter = input(str("Enter the letter to find its position:"))
tuple = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

def find_position(char):
    if len(char) == 1:
        if char in tuple:
            print(tuple.index(char)+1)
    else:
        print("Please enter a single character")


find_position(letter.lower())