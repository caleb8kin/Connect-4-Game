#P2 of c4game.py Assignment 3

from connect4 import *

def main():
    didTypeQuitYet = False                                  # this while loop keeps new games available. 
    while not didTypeQuitYet:
        size_of_boardgame = input('Size of game board: ')   # inputs could look like '4,6' for exmaple. 
        if size_of_boardgame == 'quit':
            print('Thanks for playing!')
            break
        else:                                              # if good input for board, create it. 
            size_of_boardgame = size_of_boardgame.replace(' ', '') 
            size_of_boardgame = size_of_boardgame.split(',')
            numRow = int(size_of_boardgame[0])
            numCol = int(size_of_boardgame[1])
            the_grid = makeGrid(numRow,numCol)
            toString(the_grid)                              # shows the grid so the first player can visualize their possible moves
            current_player = 'red'                          # game always starts with X (red) player. 
            game_in_progress = True
            numMoves = 0                                    # counter for final win statement. 
            while game_in_progress:                         # when some player wins, this is False and thus unsatisfied.                          
                for row in the_grid:
                    if 'empty' in row:                      # this makes sure that the player dropped in to a spot that is not arleady occupied.
                        whereToPlay = int(input(current_player + " what column to drop: "))
                        if play(the_grid, whereToPlay, current_player):
                            numMoves += 1                   # increment the counter. 
                            toString(the_grid)              # update the board game to assist in making next moves.
                            if win(the_grid, whereToPlay) == 'empty':
                                if current_player == 'black':   # swaps player's turn.
                                    current_player = 'red'
                                else:
                                    current_player = 'black'   
                                break
                            else:
                                toString(the_grid)          # win has been detected. Print winnner has won after the incremented counter's value.
                                print(current_player, 'has won after', numMoves, 'moves!')
                                game_in_progress = False    # change the boolean, and go back to asking baord game size for next game.  
                                break        
                        else:
                            print('That was an invalid move.') # the player dropped a checker in a full column. However, no safe guard against input column out of range.
                            break                              # breaks the for loop    
                    else:
                        print('The game is a tie!')         # found that there were no elements in all rows and colums that read 'empty',
                        game_in_progress = False            # therefore, game must have been a tie. Game in progress is now False. 
                        break

if __name__ == "__main__":                                  # defining a main guard. 
    main()                                                  # called main function.  
