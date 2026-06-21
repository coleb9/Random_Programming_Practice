import random

words = ["elsa", "hello", "car", "knife"]

word = random.choice(words)
lives = 5

print("Let's Play Hangman!")

user_progress = []
for char in word:
    user_progress.append("_")


def check(user_guess, lives):
    if user_guess in word:
        for i in range(len(word)):
            if user_guess == word[i]:
                user_progress[i] = user_guess
    else:
        lives -= 1

    return lives


def print_current_word():
    printable = ""
    for char in user_progress:
        printable += char
    print(printable)


while lives > 0:
    user_guess = input("Enter a guess: ")

    # Optional: ensure only one letter is entered
    if len(user_guess) != 1:
        print("Please enter a single letter.")
        continue

    lives = check(user_guess, lives)

    print_current_word()
    print(f"Current Lives Remaining: {lives}")

    if "_" not in user_progress:
        print("YOU WIN!")
        break

if lives == 0:
    print(f"YOU LOSE! The word was '{word}'")