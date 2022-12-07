#P1 of connect4.py Assignment 3

def makeGrid(nRows, nCols):
    if 4 <= nRows and nRows <= 10 and 4 <= nCols and nCols <= 10:
        return [['empty' for i in range(nCols)] for j in range(nRows)]
    else:
        print('remake grid')

def play(grid, column, checker) -> bool:
    if 0 <= column <= len(grid):
        for row in range(len(grid) - 1, -1, -1):
            if grid[row][column] != 'empty':
                continue
            elif grid[row][column] == 'empty':
                grid[row][column] = checker 
                return True 
            else:
                continue
    else:
        print('Column out range.')
        return False        

def win(grid, column) -> str:
    #Set up variables
    nRows = len(grid)       
    nCols = len(grid[0])
    turn_piece = ''  
    
    #loop thorough last column played to find the colour we are on
    for row in range(0, len(grid), 1):
        if grid[row][column] != 'empty':
            turn_piece = grid[row][column]
            break

    #check horizontal win
    for row in range(nRows):
        for col in range(nCols - 3):
            if (turn_piece == grid[row][col]) \
                and (turn_piece == grid[row][col + 1]) \
                and (turn_piece == grid[row][col + 2]) \
                and (turn_piece == grid[row][col + 3]):
                    return grid[row][col]
            else: 
                continue
                
    #check for vertical win
    for row in range(nRows - 3):
        for col in range(nCols):
            if (turn_piece == grid[row][col]) \
                and (turn_piece == grid[row + 1][col]) \
                and (turn_piece == grid[row + 2][col]) \
                and (turn_piece == grid[row + 3][col]):
                    return grid[row][col]
            else:
                continue 

    #check for diagonal up to the right 
    for row in range(nRows):
            for col in range(nCols - 3):
                if (turn_piece == grid[row][col]) \
                    and (turn_piece == grid[row - 1][col + 1]) \
                    and (turn_piece == grid[row - 2][col + 2]) \
                    and (turn_piece == grid[row - 3][col + 3]):
                        return grid[row][col]
                else: 
                    continue
                 
    #check for diagonal up to the left
    for row in range(nRows):
            for col in range(3, nCols):
                if (turn_piece == grid[row][col]) \
                    and (turn_piece == grid[row - 1][col - 1]) \
                    and (turn_piece == grid[row - 2][col - 2]) \
                    and (turn_piece == grid[row - 3][col - 3]):
                        return grid[row][col]
                else: 
                    continue 

    #if we got this far, there is no winner yet.. so return empty        
    return 'empty'               

def toString(grid):
    counter = 0
    for row in grid:
        row_to_print = '|'
        for column in row: 
            if column == 'red':
                row_to_print += 'X'
            elif column == 'black':
                row_to_print += 'O'
            else:
                row_to_print += ' ' 
        row_to_print += '|'
        row_to_print += str(counter)
        counter += 1 
        print(row_to_print)
    nCols = len(grid[0])
    print('+'+'-'*nCols+'+')
    bottomString = ' ' 
    for x in range(nCols):
        bottomString += str(x)
    print(bottomString, ' ')


