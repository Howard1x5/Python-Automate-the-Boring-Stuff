

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# two loops for rows and columns starting with columns

for column in range(len(grid[0])):         # take the 0th column in the total range of grid
    for row in range(len(grid)):           # take the 0th row in the total range of grid
        print(grid[row][column], end='')    # print grid[column:row] and use end='' to stop new line from being created
    print()                                # print newline once through first set of columns