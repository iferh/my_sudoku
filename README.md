# My sudoku
A sudoku game with a "new grid maker" and a "solver" based on backtracking.

## Overview
This project was created to practice using backtracking algorithms in Python. The project includes a function to make a new board, and a function to solve the board using backtracking. The game interface was made using Pygame. 

The project was inspired by the Python Sudoku Solver [video](https://www.youtube.com/watch?v=eqUwSA0xI-s&t) by Tech-With-Tim and the Python Sudoku Solver [video](https://www.youtube.com/watch?v=G_UYXzGuqvM&t) by Computerphile, and followed part of their code, as well as the algorithm to generate random sudoku board made by [Alain T.]( https://stackoverflow.com/users/5237560/) on [this stackoverflow question](https://stackoverflow.com/questions/45471152).

## Instructions
To play run Game.py. Click an empty square to select it. Pressing a number will add the number as a draft to the selected square. Pressing enter will add the draft number to the board if it is correct or add 1 to the mistake count if it is incorrect. Pressing the “new puzzle” button will create a new game with a random sudoku board. Pressing the “solve puzzle” button will display the solved board.
