
from itertools import chain 


x = [
 ['a1',	'a2',	'a3',	'a4',	'a5',	'a6',	'a7',	'a8'],
['b1',	'b2',	'b3',	'b4',	'b5',	'b6',	'b7',	'b8'],
['c1',	'c2',	'c3',	'c4',	'c5',	'c6',	'c7',	'c8'],
['d1',	'd2',	'd3',	'd4',	'd5',	'd6',	'd7',	'd8'],
['e1',	'e2',	'e3',	'e4',	'e5',	'e6',	'e7',	'e8'],
['f1',	'f2',	'f3',	'f4',	'f5',	'f6',	'f7',	'f8'],
['g1',	'g2',	'g3',	'g4',	'g5',	'g6',	'g7',	'g8'],
['h1',	'h2',	'h3',	'h4',	'h5',	'h6',	'h7',	'h8']
]
####setting a dummy value to a global variable
turn = 'A'

##### use this function to swap the values of X & O when needed
def flipTurns(turn):
    if turn == ' X':
        turn = ' O'
    elif(turn == ' O'):
        turn = ' X'       
    return turn

#### Logic: Player X can place a chip adjacent to a O chip provided the row or column in which
#### the chip is placed also has a X

########### Checking if there is same chip in the row the chip is placed ######
#### assuming X is playing
##### 'r' is for checking if there is X chip in the right 
###### 'l' is for left

def checkRow(row,col, direction, turn):
    
    check = turn

    if(direction == "r"):
        for i in range(col+2,8,1):
            if(x[row][i] == check):
                return "true"

    if(direction == "l"):
        for i in range(col-2, -1, -1):
            if(x[row][i] == check):
                print("checking ", i , " with value ",x[row][i] )
                return "true"
    return "false"

##### 'u' is for checking if there is X chip in the upper roes in the same column 
###### 'd' is for checking bottom rows
def checkCol(row,col, direction, turn):
    check = turn

    if(direction == "u"):
        for i in range(row-2,-1,-1):
            if(x[i][col] == check):
                return "true"

    if(direction == "d"):
        for i in range(row+2, 8, 1):
            if(x[i][col] == check):
                return "true"
    return "false"

###### validate if the adjacent chip is opposite types and if there is same chip in either same row and column

def validateMove(Row, column, turn):
    check = flipTurns(turn)
     
    #check right column
    colRight = column + 1
    if(colRight >= 0 and colRight <= 7):
        if(x[Row][colRight] == check):
            if(checkRow(Row,column,"r",turn) == "true"):
                return "true"

    #check left column
    colLeft = column - 1
    if(colLeft >= 0 and colLeft <= 7):
        if(x[Row][colLeft] == check):
            if(checkRow(Row,column,"l",turn) == "true"):
                return "true"
               
                    
    #check bottom row
    bottomTop = Row + 1
    if(bottomTop >= 0 and bottomTop <= 7):
        if(x[bottomTop][column] == check):
            if(checkCol(Row,column,"d",turn) == "true"):
                return "true"
     #check top row
    TopRow = Row - 1
    if(TopRow >= 0 and TopRow <= 7):
        if(x[TopRow][column] == check):
            if(checkCol(Row,column,"u",turn) == "true"):
                return "true"

    return "false"     

def flipCoins(Row,Column, turn):
    check = flipTurns(turn) 
    x[Row][Column] = turn
    #upward rows 
    if(Row-1 >-1): ## checking for boundary condition
        if(x[Row-1][Column] == check):
            if(checkCol(Row,Column,"u",turn) == "true"):
                for i in range(Row-1,0,-1):                
                    #print("upward rows  Checking: ", i, " ",Column)
                    if(x[i][Column] == check):
                        x[i][Column] = turn
                    else:
                        break

    #downward rows 
    if(Row+1 < 8):
        if(x[Row+1][Column] == check):
            if(checkCol(Row,Column,"d",turn) == "true"): 
                for i in range(Row+1,8,1):
                    #print("downward rows Checking: ", i, " ",Column)
                    if(x[i][Column] == check):
                        x[i][Column] = turn
                    else:
                        break 

    #left columns
    if(Column-1 >-1):
        if(x[Row][Column-1] == check):
            if(checkRow(Row,Column,"l",turn) == "true"):
                for i in range(Column-1,0,-1):
                # print("Left columnsChecking: ", i, " ",Row)
                    if(x[Row][i] == check):
                        x[Row][i] = turn
                    else:
                        break 

    #Right columns
    if(Column+1 <8): 
        if(x[Row][Column+1] == check):
            if(checkRow(Row,Column,"r",turn) == "true"):   
                for i in range(Column+1,8,1):
                    if(x[Row][i] == check):
                        #print(i, " column has value", x[Row][i], " &  is checked for ", check)
                        x[Row][i] = turn
                    else:
                        break

### Calculate the score 
def Score():
    XScore = 0
    YScore = 0
    for i in range(0,8, 1):
        XScore += x[i].count(' X')
        YScore += x[i].count(' O')

    print("X Score: ", XScore)
    print("O Score: ", YScore)
    return XScore+YScore

## Print Matrix()
def printMatrix():
    for i in range(0,8, 1):
        print(x[i])

move = '0'
## get the move
def getMove():
    present = False
    
    while(present == False):
        move = input("Enter the spot you want to place your chip: ")   
        if(move == "P"):
                return "P"
        else:
            present = {move}.issubset(chain.from_iterable(x)) 
            if(present):
                print(" You selected " + move ," it is present in the matrix ", str(present))
                return move
            else:
                print("Please choose an appropriate value.....")


def playGame(turn):
    Row = -1,
    Column = -1
    isMoveValid = "false"
    changeBoard = False
    while(isMoveValid == "false"):
        
        move = getMove()
        if(move == "P"):
            print("Player ", turn, " choose to pass the move. ")
            changeBoard = False
            isMoveValid = "true"
        else:
            idx =  [(index, row.index(move)) for index, row in enumerate(x) if move in row]
            #print("index: " + str(idx) )
            Row = int(str(idx).split(',')[0].split('(')[1])
            Column = int(str(idx).split(',')[1].split(')')[0])
            valid = validateMove(Row,Column,turn)
            if(valid == "true"):
                changeBoard = True
            if(valid == "false"):
                print("Invalid move, please choose another spot.......")
                print("Remember the spot you choose must have an ", flipTurns(turn), " adjacent to it and it should atleast have one ", turn, " chip in the same row or column you choose.........")
            isMoveValid = valid
    if(changeBoard):
        flipCoins(Row, Column, turn)
 

def StartGame():
    
    turn = ' O'
    x[4][4] = ' X'
    x[5][4] = ' O'
    x[4][5] = ' O'
    x[5][5] = ' X'
    for i in range(0,8, 1):
        print(x[i])
    

    TotalScoreM = 0
    while TotalScoreM < 65:
        turn = flipTurns(turn)
        print("Player ", turn, " playing.........")
        playGame(turn)
        printMatrix()
        TotalScoreM = Score()
        

        
    
StartGame()







