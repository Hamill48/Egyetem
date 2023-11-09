import random

def chooseWord():
    wordList = ["apple", "sun", "programming", "moon", "dinosaur"]
    return random.choice(wordList)

def displayWord(word, guessedLetters):
    display = ""
    for letter in word:
        if letter in guessedLetters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def wordGame():
    wordToGuess = chooseWord()
    guessedLetters = []
    attempts = 0

    print("Guess the word:", displayWord(wordToGuess, guessedLetters))

    while True:
        guess = input("Is it in the word: ").lower()

        if guess in guessedLetters:
            print("You already asked this letter.")
            continue

        guessedLetters.append(guess)

        if guess in wordToGuess:
            print("Yes:", displayWord(wordToGuess, guessedLetters))
        else:
            print("No")

        attempts += 1

        if set(wordToGuess.replace(" ", "")) <= set(guessedLetters):
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break

if __name__ == "__main__":
    wordGame()