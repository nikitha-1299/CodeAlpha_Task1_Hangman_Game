import random

# List of predefined words
words = ["python", "computer", "coding", "program", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_incorrect_guesses = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

# Create blanks for the word
display_word = ["_"] * len(word)

while incorrect_guesses < max_incorrect_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses:", incorrect_guesses)
    print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    # Check whether input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in display_word:
    print("\n================================")
    print("🎉 CONGRATULATIONS!")
    print("You guessed the word:", word)
    print("================================")

else:
    print("\n================================")
    print("GAME OVER!")
    print("The correct word was:", word)
    print("================================")
