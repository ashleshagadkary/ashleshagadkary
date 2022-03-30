import random
name = input("Enter your name: ")
print("Hello " + name + "! " + "Welcome to Hangman.")
print("--------------")

word_list = ["apple", " banana", "jug", "king", "place", "joke", "fool", "like", "stone", "joy", "cold"]

random_word = random.choice(word_list)

for x in random_word:
    print("_", end=" ")


def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif wrong == 3:
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif wrong == 6:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")

def print_word(guessed_letters):
    counter = 0
    right_letters = 0
    for char in random_word:
        if char in guessed_letters:
            print(random_word[counter], end=" ")
            right_letters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return right_letters

def print_lines():
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")

length_of_word_to_guess = len(random_word)
wrong_guesses = 0
current_guess_index = 0
letters_guessed = []
current_right_letters = 0

while wrong_guesses != 6 and current_right_letters != length_of_word_to_guess:
    print("\nLetters guessed so far: ")
    for letter in letters_guessed:
        print(letter, end=" ")
    user_guess = input("\nGuess a letter: ")
    if random_word[current_guess_index] == user_guess:
        print_hangman(wrong_guesses)
        current_guess_index += 1
        letters_guessed.append(user_guess)
        current_right_letters = print_word(letters_guessed)
        print_lines()
    else:
        wrong_guesses += 1
        letters_guessed.append(user_guess)
        print_hangman(wrong_guesses)
        current_right_letters = print_word(letters_guessed)
        print_lines()

print("Game is over!")
