def myFunction(string, character):
    characterInString = 0

    for letter in string:
        if character in letter:
            characterInString += 1
    return characterInString

print(myFunction('almafa', 'a'))