# Character Picture Grid

# Say you have a list of lists where each value in the inner lists is a one-character string, like this:

# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]

# Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

# Copy the previous grid value, and write code that uses it to print the image.

# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

# Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will finish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on. The last thing your program will print is grid[8][5].

# Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.

# Observations
    # grid is a list of lists (grid[row][col])
    # print order needs to be “column by column”
    # nested loop is needed
    # two indices—one for rows and one for columns.
    ## First, loop over the columns (left to right).
    ## Then, inside that loop, iterate over the rows (top to bottom).
    ## I need the following loops:
    ### An outer loop that controls which column we're printing.
    ### An inner loop that prints each row for that column.

# for column in range(length(grid[0])) # loop columns left to right
    # for row in range(length(grid))   # loop rows top to bottom
        # print(grid[row][col], end='') # print character w/o new line
    # print()                          # new line

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for column in range(len(grid[0])): # loop columns left to right
    for row in range(len(grid)):   # loop rows top to bottom
        print(grid[row][column], end='') # print character w/o new line
    print()                          # new line

    
