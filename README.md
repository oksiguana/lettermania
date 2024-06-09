# Lettermania

Lettermania is a deductive logic game inspired by Bagels, where you must guess a letter combination based on clues.

## Game Description

In Lettermania, the player needs to guess a secret combination of letters. The game will provide clues after each guess to help the player deduce the correct combination. The clues are as follows:

- **Hit:** One letter is correct and in the right position.
- **Pip:** One letter is correct but in the wrong position.
- **Miss:** No letter is correct.

For example, if the secret letter combination is `CAB` and the player's guess is `BAL`, the clues would be `Hit Pip`.

## How to Play

1. The game will think of a 3-letters combination with no repeated letters.
2. The player has a limited number of guesses to figure out the combination.
3. After each guess, the game will provide clues based on the guess.
4. Use the clues to deduce the correct letter combination.

## Installation

To play Lettermania, follow these steps:

1. **Clone the repository:**
```sh
git clone https://github.com/oksiguana/lettermania.git
```
2. **Navigate to the project directory:**
```sh
cd lettermania
```
3. **Run the game:**
```sh
python lettermania.py
```

## Acknowledgements

Inspired by the game Bagels.