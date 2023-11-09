vowels = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']

def vowelRemover(string):
    wordWithoutVowels = ''
    for letter in string:
        if letter not in vowels:
            wordWithoutVowels += letter
    return wordWithoutVowels

print(vowelRemover('Szentségtelenítés'))