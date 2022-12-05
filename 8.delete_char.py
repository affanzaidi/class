# delete a desired character from a string

data = input(str("Enter a string:"))
del_char = input(str("enter the letter to remove from the string:"))

def delete_character(word, char):
    new_string = ""
    for letter in word:
        if (letter != char):
            new_string += letter
    result = new_string
    print(result)
        

        # print(letter)


delete_character(data, del_char)