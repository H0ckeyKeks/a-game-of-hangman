# hangman
This is a code for the well-known game hangman.

I created a list of words where the program can randomly choose a word from. The user is asked for input which can only be one alphanumeric character. The program checks if the input is in the randomly chosen word and substract this turn from the number of turns the user has. If the user has no turns left, the program will print out a message, telling the user that there are no turns left, that the user has lost the game and what the correct word was.

If the user has guessed one character correctly, the programm will print the letter and ask the user for another input. The program also checks if the letter the user wrote was already used and will print out a respective message.

If the user guessed the word correctly, the programm will print out another message, telling the user the correct word and that the user has won.
