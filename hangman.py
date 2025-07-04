import random

# List of predefined words
word_list = ["apple", "train", "house", "chair", "plant"]

# Select a random word
secret_word = random.choice(word_list)

# Variables to track guesses
guessed_letters = []
wrong_guesses = 0
max_guesses = 6      

# Display version of word
display_word = ["_" for _ in secret_word]

print("🎮 Welcome to Hangman Game!") 
print("Guess the word, one letter at a time.")
print("You can make up to 6 wrong guesses.\n")

# Game loop
while wrong_guesses < max_guesses and "_" in display_word:
    print("Word: ", " ".join(display_word))
    print("Guessed letters: ", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    # Check valid input
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.\n")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("✅ Correct!\n")
    else:
        wrong_guesses += 1
        print(f"❌ Incorrect! You have {max_guesses - wrong_guesses} guesses left.\n")

# Result
if "_" not in display_word:
    print("🎉 You won! The word was:", secret_word)
else:
    print("😢 You lost! The word was:", secret_word)

