def spell_check(s):
    vowels = 'aeiouAEIOU'
    words = s.split()

    for i, word in enumerate(words):
        if word == 'a':
            if len(words) > i+1 and words[i+1][0] in vowels:
                words[i] = 'an'
        s = ' '.join(words)
    return s


print(spell_check("this is an apple"))