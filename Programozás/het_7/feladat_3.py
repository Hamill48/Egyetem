string = input('Write a string: ')
lowerString = string.lower()
noWhiteSpaceString = lowerString.replace(' ', '')

def backwardWord():
    backWard = noWhiteSpaceString[::-1]
    return backWard

def isPalindrom():
    if backwardWord() == noWhiteSpaceString:
        print('The string is palindrom!')
    else: 
        print('The string is not palindrom!')

isPalindrom()