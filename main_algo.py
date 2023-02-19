# The main algorithm to be used with FE.
import numpy as np

# the board representation ensuring summation of a row/col/diag is 15
board = np.array([[8,3,4],[1,5,9],[6,7,2]])

# print(board)

# Lists to store the moves of each player
moves_0=[]
moves_X=[]

if __name__== '__main__':
    print("Game begins")