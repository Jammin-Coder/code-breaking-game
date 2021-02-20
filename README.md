# code-breaking-game
A terminal based code breaking game.

To use this program, just run it with a python interpreter.

python Code-Breaking-Game.py -m 5 -l 4

-m is the max value in the code, 0 to -m. -l is the length of the code.
To guess the code, start by passing in any number within range of the max value.
The program will give an output of O's and X's, depending on how accurate your guess was.
If you get an X in the output, that means you have a number in the correct index in the code.
If you get an O in the output, that means you have the right number, but it is in the wrong index.
If you get nothing, then you have not correct numbers.

Example:
My guesss >> 1010
Result >> OXX
This tells me that there are 2 numbers in the correct place, and one of them is not.
One number is not used.
My guess >> 0012
Reuslt >> OXXO
This tells me that 2 of the numbers are in the correct index, and 2 are not.
My guess >> 2010
Result >> CORRECT
