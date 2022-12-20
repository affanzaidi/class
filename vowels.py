# string = "hello"
# vowels = ('a', 'e','i','o','u')
#
# for i in  string:
#     if i in vowels:
#         print("nnot 1")
    # elif string[len(string)-1] in vowels:
    #     print("is vowel")


# String = string[0].upper() + string[1:len(string)-1] + string[len(string)-1].upper()

# print(String)


def capitalize_vowels(s):
  vowels = 'aeiouAEIOU'
  if s[0] in vowels:
    s = s[0].upper() + s[1:]
  if s[-1] in vowels:
    s = s[:-1] + s[-1].upper()
  return s

print(capitalize_vowels("aeiou"))