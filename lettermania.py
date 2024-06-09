"""Lettermania.
A deductive logic game inspired by Bagels, where you must guess a letter combination based on clues."""

import random

NUM_LETTERS = 3
MAX_GUESSES = 15


def main():
    print('''Lettermania, a deductive logic game inspired by Bagels.


I am thinking of a {}-letters combination with no repeated letters.
Try to guess what it is. Here are some clues:
When I say:   That means:
  Pip         One letter is correct but in the wrong position.
  Hit         One letter is correct and in the right position.
  Miss        No letter is correct.

For example, if the secret letter combination was CAB and your guess was BAL, the
clues would be Hit Pip.'''.format(NUM_LETTERS))

    while True: # Main game loop.
        # This stores the secret combination of letters the player needs to guess:
        secretLet = getSecretLet()
        print('I have thought up a letter combination.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
                guess = ''
                # Keep looping until they enter a valid guess:
                while len(guess) != NUM_LETTERS or guess.isdecimal():
                    print('Guess #{}: '.format(numGuesses))
                    guess = input('> ').upper()
            
                clues = getClues(guess, secretLet)
                print(clues)
                numGuesses += 1

                if guess == secretLet:
                    break # They're correct, so break out of this loop.
                if numGuesses > MAX_GUESSES:
                    print('You ran out of guesses.')
                    print('The answer was {}.'.format(secretLet))
            
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').upper().startswith('Y'):
                break
        print('Thanks for playing!')
    

def getSecretLet():
    """Returns a string made up of NUM_LETTERS unique random letters."""
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') # Create a list of letters from a to z.
    random.shuffle(letters) # Shuffle them into random order.

    # Get the first NUM_LETTER letters in the list for the secret letters:
    secretLet = ''
    for i in range(NUM_LETTERS):
        secretLet += str(letters[i])
    return secretLet


def getClues(guess, secretLet):
    """Returns a string with the Pip, Hit, Miss clues for a gues
    and a secret letter combination."""
    if guess == secretLet:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretLet[i]:
            # A correct letter is in the correct place.
            clues.append('Hit')
        elif guess[i] in secretLet:
            # A correct letter is in the incorrect place.
            clues.append('Pip')
    if len(clues) == 0:
        return 'Miss' # There are no correct letters at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # does not give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)
    

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()