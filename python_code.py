import numpy as np
import random

"Board constants"
# BLANK CELL = 2
# X = 3
# O = 5


# The 3*3 board
board = np.array([[1,2,3],[4,5,6],[7,8,9]])

# States of each cell
"Initially all cells are BLANK so filled with 2s"
states = np.array([[2,2,2],[2,2,2],[2,2,2]])

# Functions required

def make2():
    """Returns 5 if central square is empty otherwise returns any noncorner blank square : 2,4,6,8"""
    if states[1,1] == 2:
        return board[1,1]
    else:
        if states [0,1]==2 or states[1,0]==2 or states[1,2]==2 or states[2,1]==2:
            "All corner squares are empty return any one of them."
            emptySquares = [[0,1],[1,0],[1,2],[2,1]]
            chosen = random.choice(emptySquares)
            emptySquares.remove(chosen)
            return board[chosen]
    


def Posswin():
    """Returns 0 if the player cannot win on his next move otherwise it returns number of square constituting the winning move"""

    product=1
    counter=0
   
    # Scan column 1
    for i in [(0,0),(1,0),(2,0)]:
        if states[i]==2:
            counter=counter+1
            emptycell=i
        if counter == 1:
            for i in [(0,0),(1,0),(2,0)]:
                product = product * states[i]
            if product == 18 or product == 50:
                return emptycell


    product=1
    counter=0
    
    # Scan row 1
    for i in [(0,0),(0,1),(0,2)]:
        if states[i]==2:
            counter=counter+1
            emptycell=i
    if counter == 1:
            for i in [(0,0),(0,1),(0,2)]:
                product = product * states[i]
            if product == 18 or product == 50:
                return emptycell


    product=1
    counter=0

    # Scan column 2
    for i in [(0,1),(1,1),(2,1)]:
        if states[i]==2:
            counter=counter+1
            emptycell=i
    if counter == 1:
        for i in [(0,1),(1,1),(2,1)]:
            product = product * states[i]
        if product == 18 or product == 50:
                return emptycell


    product=1
    counter=0
    
    # Scan row 2
    for i in [(1,0),(1,1),(1,2)]:
        if states[i]==2:
            counter=counter+1
            emptycell=i
    if counter == 1:
        for i in [(1,0),(1,1),(1,2)]:
            product = product * states[i]
        if product == 18 or product == 50:
                return emptycell


    product=1
    counter=0

    # Scan column 3
    for i in [(0,2),(1,2),(2,2)]:
        if states[i]==2:
            counter=counter+1
            emptycell=i
    if counter == 1:
        for i in [(0,2),(1,2),(2,2)]:
            product = product * states[i]
        if product == 18 or product == 50:
                return emptycell


    product=1
    counter=0
    
    # Scan row 3
    for i in [(2,0),(2,1),(2,2)]:
        if states[i]==2:
            counter=counter+1
            emptycell=i
    if counter == 1:
        for i in [(2,0),(2,1),(2,2)]:
            product = product * states[i]
        if product == 18 or product == 50:
            return emptycell


    product=1
    counter=0
    
    # Scan Diagonal 1
    for i in [(0,0),(1,1),(2,2)]:
        if states[i]==2:
            counter=counter+1
            emptycell=i
    if counter==1:
        for i in [(0,0),(1,1),(2,2)]:
            product = product*states[i]
        if product == 18 or product==50:
            return emptycell
    product=1
    counter=0

    # Scan Diagonal 2
    for i in [(0,2),(1,1),(2,0)]:
        if states[i]==2:
            counter=counter+1
            emptycell=i
        if counter==1:
            for i in [(0,2),(1,1),(2,0)]:
                product = product*states[i]
            if product == 18 or product==50:
                return emptycell
    product=1
    counter=0

    # if none other conditions satisfies
    return 0


    


def go(n,player):
    """Makes a move in square n"""
    x=n[0]
    y=n[1]
    if player==1:
        states[x,y]=3
        return 1
    elif player==2:
        states[x,y]=5
    pass





# Game begins
if __name__=='__main__':
    "Odd moves are played by player 1(X) and even moves are played by player 2(O)"
    # Move 1
    go((0,0),1)
    print(states)
    print("\n\n\n")

    # Move 2
    if states[1,1]==2:
        go((1,1),2)
    else:
        go((0,1),2)
    print(states)
    print("\n\n\n")

    # Move 3
    if states[2,2]==2:
        go((2,2),1)
    else:
        go((0,2),1)
    print(states)
    print("\n\n\n")
    
    # Move 4
    m=Posswin()
    if m != 0:
        go(m,2)
    else:
        go(make2(),2)
    print(states)
    print("\n\n\n")

    # Move 5
    if states[m] != 5:
        go(m,1)
    else:
        m=Posswin()
        if m!= 0:
            go(m,1)
        elif states[2,0] == 2:
            go((2,0),1)
        else:
            go((0,2),1)
    print(states)
    print("\n\n\n")

    # Move 6
    m=Posswin()
    if m!=0 :
        go(m,2)
    else:
        n=Posswin()
        if n!=0:
            go(n,2)
        else:
            go(make2(),2)
    print(states)
    print("\n\n\n")

    # Move 7
    m=Posswin()
    if m!=0:
        go(m,1)
    else:
        n=Posswin()
        if n!=0:
            go(n,1)
        else:
            for i in range(0,3,1):
                for j in range(0,3,1):
                    if states[i,j]==2:
                        go([i,j],1)
                        break
    print(states)
    print("\n\n\n")

    # Move 8
    m=Posswin()
    if m!=0:
        go(m,1)
    else:
        n=Posswin()
        if n!=0:
            go(n,1)
        else:
            for i in range(0,3,1):
                for j in range(0,3,1):
                    if states[i,j]==2:
                        go([i,j],1)
                        break
    print(states)
    print("\n\n\n")
    
    # Move 9
    m=Posswin()
    if m!=0:
        go(m,1)
    else:
        n=Posswin()
        if n!=0:
            go(n,1)
        else:
            for i in range(0,3,1):
                for j in range(0,3,1):
                    if states[i,j]==2:
                        go([i,j],1)
                        break
    print(states)
    print("\n\n\n")
    
        



        