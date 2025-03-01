"""Table Printer

Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose

Hint: your code will first have to find the longest string in each of the inner lists so that the whole column can be wide enough to fit all the strings. You can store the maximum width of each column as a list of integers. The printTable() function can begin with colWidths = [0] * len(tableData), which will create a list containing the same number of 0 values as the number of inner lists in tableData. That way, colWidths[0] can store the width of the longest string in tableData[0], colWidths[1] can store the width of the longest string in tableData[1], and so on. You can then find the largest value in the colWidths list to find out what integer width to pass to the rjust() string method."""

# Project Breakdown: 
# printTable() - take list of strings and print in organized table with each column Rjustified
# it is essentially taking each list and creating three columns and 4 rows that are Rjustified according to the last letter in each string. There is one space between each column
# based on the hint the process will be
## find longest string in each inner list and store max width
### colWidths = [0] * len(tableData)

# How can we find the longest string in each inner list?
## loop through all indexes in the tableData list starting with sublist 0 according to the example above there are 3 sublists but that number is arbitrary because I can just set the table data to an incrementing variable such as i
##  for i in range(length(tableData[]))
###      Check the length of each word and store largest word length in integer form in colWidth list starting in the 0th position
###     for word in range(length(tableData[0,word]
#### Evaluate the length of the string and save the number 
####    if colWidth[0] < len(word)
####    colWidth[0] = len(word)(which is the length pulled from the string at tableData[0,n])
### Iterate to the next sublist in tableData
###     tableData[i] = i + 1


def printTable(tableData):
    colWidths = [0] * len(tableData)  # Step 1: Store max width of each column

    # Step 2: Find the longest string in each column
    for i in range(len(tableData)):  
        for word in tableData[i]:  
            colWidths[i] = max(colWidths[i], len(word))  

    # Step 3: Loop through rows instead of columns
    for rowIndex in range(len(tableData[0])):  # Number of rows = length of first sublist
        for colIndex in range(len(tableData)):  # Loop through each column
            print(tableData[colIndex][rowIndex].rjust(colWidths[colIndex]), end="  ")  
        print()  # Newline after printing each row

# Example Data
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

