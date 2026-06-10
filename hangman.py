import random

words = ["apple", "mango", "grapes", "banana", "orange"]

word = random.choice(words)
guessed = []
attempt_count = 0

print("--- Welcome to Hangman Game ✨ ---")

while True:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord 🙌:", display)

    if "_" not in display:
        print("\nCongratulations 🎉! You guessed the word:", word)
        print("Total Attempts:", attempt_count)
        
        break

    guess = input("Enter a letter: ").lower()
    attempt_count += 1

    if guess in word:
        if guess not in guessed:
            guessed.append(guess)
        print("Correct 😍!")
    else:
        print("Wrong 😢! Try Again.")