# importing required libraries
from random import randint

# getting the board to initialize the game
def startTheGame():
    board=[[0 for i in range(4)] for j in range(4)]
    return board

# for putting new 2 in the Board
def add2(board):
    row=randint(0,3)
    col=randint(0,3)
    
    while board[row][col] != 0:
        row=randint(0,3)
        col=randint(0,3)
    
    board[row][col] = 2

# Getting the current state of Game 
# Won , Lost or Game not over
# Check Whether We Lost , Win or Game is not over yet
def getCurrentStateOfGame(board):
    
    # check if 2048 present in the board
    for row in range(4):
        for col in range(4):
            
            if board[row][col] == 2048:
                return "WON"
    
    # check if empty cell is Present in board
    for row in range(4):
        for col in range(4):
            
            if board[row][col] == 0:
                return "Game Not Over"

    # checking for submatrix of 3x3
    for row in range(3):
        for col in range(3):
            if board[row][col] == board[row+1][col] or board[row][col] == board[row][col+1]:
                return "Game Not Over"
            
    # checking if same value present in adjacent col of row 4
    for col in range(3):
        row=3
        if board[row][col]==board[row][col+1]:
            return "Game Not Over"
        
    # checking if same value present in adjacent row of col 4
    for row in range(3):
        col=3
        if board[row][col] == board[row+1][col]:
            return "Game Not Over"
        
        
    return "LOST"

# Compress Function
# For shifting the empty cells at Last
# return True if there is a change in the Board else return False
def compress(board):
    newBoard=[[0 for col in range(4)] for row in range(4)]
    changedOrNot=False
    for row in range(4):
        pos=0
        for col in range(4):
            if board[row][col] != 0:
                newBoard[row][pos]=board[row][col]
                if col != pos:
                    changedOrNot=True
                pos+=1
                
    return newBoard,changedOrNot

# Merge Function
# Merges the adjacent Cells with Equal Values
def merge(board):
    changedOrNot = False
    for row in range(4):
        for col in range(3):
            if board[row][col] == board[row][col+1]:
                board[row][col] = board[row][col] + board[row][col+1]
                board[row][col+1] = 0
                changedOrNot=True
    return board,changedOrNot


# Reverse Function
# This is Used for Right and Down Movement
# Reverses the values in the Row
def reverse(board):
    newBoard=[]
    
    for row in range(4):
        newBoard.append([])
        for col in range(4):
            newBoard[row].append(board[row][4-col-1])
    return newBoard

# TransPose Function
# This is used for Up & Down Movement
def transpose(board):
    newBoard=[]
    
    for row in range(4):
        newBoard.append([])
        for col in range(4):
            newBoard[row].append(board[col][row])
    return newBoard



# Moves
# Left Move
def leftMove(board):
    board,changedOrNot01=compress(board)
    board,changedOrNot02=merge(board)
    board,notImportant=compress(board)
    finalChanged=changedOrNot01 or changedOrNot02
    return board,finalChanged

# Right Move
def rightMove(board):
    board=reverse(board)
    board,changedOrNot01=compress(board)
    board,changedOrNot02=merge(board)
    board,notImportant=compress(board)
    board=reverse(board)
    finalChanged=changedOrNot01 or changedOrNot02
    return board,finalChanged

# Up Move
def upMove(board):
    board=transpose(board)
    board,changedOrNot01=compress(board)
    board,changedOrNot02=merge(board)
    board,notImportant=compress(board)
    board=transpose(board)
    finalChanged=changedOrNot01 or changedOrNot02
    return board,finalChanged

# Down Move
def downMove(board):
    board=transpose(board)
    board=reverse(board)
    board,changedOrNot01=compress(board)
    board,changedOrNot02=merge(board)
    board,notImportant=compress(board)
    board=reverse(board)
    board=transpose(board)
    finalChanged=changedOrNot01 or changedOrNot02
    return board,finalChanged