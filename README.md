# SudokuSolver

SudokuSolver is my first try at a Python program. It accepts a text file in 9x9 format as follows:

```
4  68    
 652   37
8 9    4 
 1 72 954
9       2
542 93 7 
 9    5 3
25   146 
    32  1
```

It then will solve the Sudoku puzzle by checking all numbers within the given cell's bounding box, then its row, then its column. If all but 1 possibility has been elminated, the cell is solved and it moves on. It loops through all cells until the puzzle is completely solved, then prints both the original and solved puzzles.

Nothing special, just wanted to try out Python.
