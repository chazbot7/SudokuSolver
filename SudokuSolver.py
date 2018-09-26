import os

# Determine file to be solved. Use current directory as a default
dir = os.getcwd()
changeDir = "N"
while changeDir == "N":
    changeDir = input("Directory for sudoku file is: {}\nIs this OK? (Y/N)".format(dir))
    if changeDir == "Y":
        print("Moving on...")
    else:
        dir = input("Specify new directory:")

file = input("Specify filename to solve:")
filepath = dir + "\\" + file
print("File to be solved: {}".format(filepath))

# Open and print the file
ogFile = open(filePath, "r")
ogFileLines = ogFile.read().splitlines()
ogFile.close()
print("Puzzle to be solved:")
for index, line in enumerate(ogFileLines):
    print(line[0:3].replace(" ", ".") + " | " + line[3:6].replace(" ", ".") + " | " + line[6:9].replace(" ", "."))
    if index in (2, 5):
        print("---------------")

solvedLines = []
for line in ogFileLines:
    solvedLines.append(list(line))

isSolved = 0

while isSolved == 0:
    for row in range(0,9):
        for col in range(0,9):
            currentCell = solvedLines[row][col]
            print("=======================================================================")
            print("Checking row {}, column {}  -  Value: {}".format(row, col, currentCell))
            if currentCell == " ":
                possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                # Check current box
                # Determine rows
                if row % 3 == 0:
                    rows = row, row+1, row+2
                elif row % 3 == 1:
                    rows = row-1, row, row + 1
                else:
                    rows = row-2, row-1, row

                # Determine columns
                if col % 3 == 0:
                    cols = col, col+1, col+2
                elif col % 3 == 1:
                    cols = col-1, col, col + 1
                else:
                    cols = col-2, col-1, col

                print("Rows to check: {}  -  Columns to check: {}".format(rows, cols))
                print("Current possibilities: {}".format(possibleValues))

                for rowCheck in rows:
                    for colCheck in cols:
                        print("Checking row {} and column {}: {}".format(rowCheck, colCheck, solvedLines[rowCheck][colCheck]))
                        if solvedLines[rowCheck][colCheck] != " ":
                            possibleValues.remove(int(solvedLines[rowCheck][colCheck]))

                print("Left over possibilities: {}".format(possibleValues))

                # Check current row
                for colCheck in range(0,9):
                    if solvedLines[row][colCheck] != " " and int(solvedLines[row][colCheck]) in possibleValues:
                        possibleValues.remove(int(solvedLines[row][colCheck]))

                print("Left over possibilities: {}".format(possibleValues))

                # Check current column
                for rowCheck in range(0, 9):
                    if solvedLines[rowCheck][col] != " " and int(solvedLines[rowCheck][col]) in possibleValues:
                        possibleValues.remove(int(solvedLines[rowCheck][col]))

                print("Left over possibilities: {}".format(possibleValues))

                # See what we have left
                if len(possibleValues) == 1:
                    print("Cell solved! Inserting {} to spot {},{} in solution...".format(possibleValues[0], row, col))
                    solvedLines[row][col] = possibleValues[0]
            else:
                print("Cell already solved. Moving on...")

    # Check if the puzzle is solved
    isSolved = 1
    for row in range(0,9):
        for col in range(0,9):
            if solvedLines[row][col] == " ":
                isSolved = 0


print("\nOriginal puzzle:")
for index, line in enumerate(ogFileLines):
    print(line[0:3].replace(" ", ".") + " | " + line[3:6].replace(" ", ".") + " | " + line[6:9].replace(" ", "."))
    if index in (2, 5):
        print("---------------")

print("\nSolved puzzle:")
for index, line in enumerate(solvedLines):
    print(str(line[0]) + str(line[1]) + str(line[2]) + " | " + str(line[3]) + str(line[4]) + str(line[5]) + " | " + str(line[6]) + str(line[7]) + str(line[8]))
    if index in (2, 5):
        print("---------------")
