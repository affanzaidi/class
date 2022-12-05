# delete duplicate from a string
data = input(str("Enter a string:"))
# del_char = input(str("enter the letter to remove from the string:"))

def delete_dups(word):
    new_string = ""
    for letter in word:
        if (letter in new_string):
            pass
        else:
            new_string=new_string+letter
    print(new_string)

delete_dups(data)


