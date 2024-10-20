import time
import random

# Making sure the program is using the system time, so that random seed is not set
# the same way everytime the script is executed
random.seed()

wordlist = ["Baum", "Waldweg", "Grün", "Sommer"]
word = random.choice(wordlist).lower() # Converting to lowercase to match input
turns = 20
guesses = ""

print("Hallo. Du hast 20 Versuche das Wort zu erraten. Es geht um das Thema 'Draußen'")

# Loop for as long as there are turns left
while turns >= 0:
    guess_char = input("Gib einen Buchstaben ein: ").lower()
    turns = turns - 1

    # Check if input is only one character
    if len(guess_char) != 1 or not guess_char.isalpha():
        print("Bitte gib einen gültigen Buchstaben ein.")
        continue

    # Check if input character was already used
    if guess_char in guesses:
        print("Diesen Buchstaben hast du bereits versucht.")

    guesses += guess_char

    display_word = ""
    for char in word:
        if char in guesses:
            display_word += char + " "
        else:
            display_word += "_ "
    print("\nWort: " + display_word.strip()) # Strip() method removes any tabs, spaces, newlines etc.

    # Condition if guess is not in word
    if char not in word:
        print("Das war leider falsch. Du hast noch " + str(turns) + " Versuche übrig.")

    # Check if word was correctly guessed
    if "_" not in display_word:
        print("Herzlichen Glückwunsch! Du hast das Wort '" + word + "' erraten!")
        break

    print("Du hast noch " + str(turns) + " Versuche übrig.\n")

    # if Player runs out of turns
    if turns == 0:
        print("0 Versuche übrig. Du hast leider verloren! Das gesuchte Wort war: " + word + ".")






