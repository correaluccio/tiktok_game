# TIK-TOK GAME
## tiktok_game is a game based in a tik-tok filter, is a simple game where you have to guess a number.

## Installation

Clone the repository using the following command:

git clone https://github.com/username/repository.git

## Usage
To play it, you have to run playGame.py

## Rules of the game
You have to choose a fesaible number, a feasible number is a number with the digits 1 to 9, and doesn't have repeated digits.
Ej: 1234 ,7654,3198, etc.
1126 isn't a feasible number.

For each number you put in the game, the game will tell you how many correct positions you have and how many correct numbers. Whit these information you have to guess the number in the minimus number of attemps.

## How works the functions in gameNumbers.py

### countOcurrences
This function takes two parametres "numberGame" and "playerNumber"
The function creates a list with the numbers choosed, and count in the var "aux", the number of ocurrences between numberGame and playerNumber.

### generateNumber
Take a random number from a list and then remove this number, then choose another, when the function take 4 numbers (digits),
return the number generater. This number is the number we will have to guess.

### fesaible_Number 
Take a number as parametrer, if the number is feasible return True, if the number isn't feasible return False.
