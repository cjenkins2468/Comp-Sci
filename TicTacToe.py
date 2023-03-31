def print_board(board): # board printing funtion
    for i in board: # this makes it so that it makes it print the board in a 3x3 grid
        print(i) #finally prints it

def player1(player1_play,board):# player 1 replacing function
    try: #breaks if not in right format meaning I can make a try catch
        player1_row = int(player1_play.split(",")[0]) # getting the row
        player1_row = player1_row-1 # making it so that the rows are are 1,2,3 not 0,1,2
        player1_col = int(player1_play.split(",")[1]) # getting the collem
        player1_col = player1_col-1# making it so that the collem are are 1,2,3 not 0,1,2
        board[player1_row][player1_col] = 'x' # replaceing!
        return True #making sure it is in the right format
    except:  #catch
        print("cannot play that must be (Row,Column)") #telling what they are doing wrong
def player2(player2_play,board):#player 2 replacing function
    try:    #breaks if not in right format meaning I can make a try catch
        player1_row = int(player2_play.split(",")[0])   # getting the row
        player1_row = player1_row-1 # making it so that the rows are are 1,2,3 not 0,1,2
        player1_col = int(player2_play.split(",")[1])   # getting the collem
        player1_col = player1_col-1 # making it so that the collem are are 1,2,3 not 0,1,2
        board[player1_row][player1_col] = 'o'# replaceing!
        return True #making sure it is in the right format
    except: # catch
        print("cannot play that must be (Row,Column)") #telling what they are doing wrong
def checkSpot(spotcheck,board): # function to check if someone alrighty played
    spotRow = int(spotcheck.split(",")[0])-1 # getting row and collem 
    spotCol = int(spotcheck.split(",")[1])-1 #getting row and collem 
    if board[spotRow][spotCol] == "-": #if blank
        return True
    if board[spotRow][spotCol] == "x" or "o": # if taken
        return False
def end(board,a): # checking if anyone won!
    if board[0][0] == a and board[0][1] == a and board[0][2] == a: # combo for a win
        return True #True if won
    if board[1][0] == a and board[1][1] == a and board[1][2] == a: # combo for a win
        return True #True if won
    if board[2][0] == a and board[2][1] == a and board[2][2] == a: # combo for a win
        return True #True if won
    if board[0][0] == a and board[1][0] == a and board[2][0] == a: # combo for a win
        return True #True if won
    if board[0][1] == a and board[1][1] == a and board[2][1] == a: # combo for a win
        return True #True if won
    if board[0][2] == a and board[1][2] == a and board[2][2] == a: # combo for a win
        return True #True if won
    if board[0][0] == a and board[1][1] == a and board[2][2] == a: # combo for a win
        return True #True if won
    if board[0][2] == a and board[1][1] == a and board[2][0] == a: # combo for a win
        return True #True if won
def player_playing(board,a): # playing loop 
    win = False # stating the loop varible
    if a == '1':# checking whos playing
        player1_play = input("player "+ a +", what do you want to play: (Row,Column)  \n") # asking for input (_,_)
    elif a == '2': # checking whos playing 
        player2_play = input("player "+ a +", what do you want to play: (Row,Column)  \n") # asking for input (_,_)
    if a == '1': # checking whos playing
        if checkSpot(player1_play,board): # spot checking (calling)
            player1(player1_play,board) # replacing
            print_board(board) # printing 'new' board
        elif checkSpot(player1_play,board) == False: # if someone alrighty played
            print("that has alrighty been played") # prints to help them understand
            player_playing(board,'1') # loops it
    elif a == '2': # checking whos playing
        if checkSpot(player2_play, board): # spot checking (calling)
            player2(player2_play,board)# replacing
            print_board(board)# printing 'new' board
        elif checkSpot(player2_play,board) == False:# if someone alrighty played
            print("that has alrighty been played")# prints to help them understand
            player_playing(board,'2')# loops it
    if a == '1': # checking whos playing
        if player1(player1_play,board): 
                return True # making sure that it is running
        elif player1_play == False:
                player_playing(board) #looping
    elif a == '2': # checking whos playing
        if player2(player2_play,board): 
                return True #making sure that it is running
        elif player2_play == False: 
                player_playing(board) #looping

def gameloop(board): #full game loop until win
    game = True # loop
    try:
        while game == True: #while loop
            if player_playing(board,'1') == True: # if player 1 played...
                if end(board,'x'): # end function to see if they won
                    print ("player 1 wins!.... restarting\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
                    main() # won 
                elif player_playing(board,'2') == True: # if didn't win then 
                    if end(board,'o'): # end function to see if they won
                        print ("player 2 wins!.... restarting\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # won
                        main() # won 
                    gameloop(board) #LOOOOOOPPPPINGGGGGGG if no one won!
    except:
        print("wrong input restarting...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        main()

def main(): # main
    board = [['-','-','-'],['-','-','-'],['-','-','-']]  # making the board list so I can print it and replace in individual places
    print_board(board) # calling the print board function
    gameloop(board) # starting the game (player v player)
main()