
def print_board(board): # board printing funtion
    for i in board: # this makes it so that it makes it print the board in a 3x3 grid
        print(i) #finally prints it

def player1(player1_play,board):# player 1 replacing function
    try: #breaks if not in right format meaning I can make a try catch
        if player1_play == "1":#finding what they played
            board[1][1] = 'x'  #replacing
        if player1_play == "2":#finding what they played
            board[1][2] = 'x' #replacing
        if player1_play == "3":#finding what they played
            board[1][3] = 'x' #replacing
        if player1_play == "4":#finding what they played
            board[2][1] = 'x' #replacing
        if player1_play == "5":#finding what they played
            board[2][2] = 'x' #replacing
        if player1_play == "6":#finding what they played
            board[2][3] = 'x' #replacing
        if player1_play == "7":#finding what they played
            board[3][1] = 'x' #replacing
        if player1_play == "8":#finding what they played
            board[3][2] = 'x' #replacing
        if player1_play == "9":#finding what they played
            board[3][3] = 'x' #replacing
        return True #making sure it is in the right format
    except:  #catch
        print("cannot play that must be (_,_)") #telling what they are doing wrong
def player2(player1_play,board):#player 2 replacing function
    try: #breaks if not in right format meaning I can make a try catch
        if player1_play == "1":#finding what they played
            board[1][1] = 'x'  #replacing
        if player1_play == "2":#finding what they played
            board[1][2] = 'x' #replacing
        if player1_play == "3":#finding what they played
            board[1][3] = 'x' #replacing
        if player1_play == "4":#finding what they played
            board[2][1] = 'x' #replacing
        if player1_play == "5":#finding what they played
            board[2][2] = 'x' #replacing
        if player1_play == "6":#finding what they played
            board[2][3] = 'x' #replacing
        if player1_play == "7":#finding what they played
            board[3][1] = 'x' #replacing
        if player1_play == "8":#finding what they played
            board[3][2] = 'x' #replacing
        if player1_play == "9":#finding what they played
            board[3][3] = 'x' #replacing
        return True #making sure it is in the right format
    except:  #catch
        print("cannot play that must be (_,_)") #telling what they are doing wrong
def checkSpot(spotcheck,board): # function to check if someone alrighty played
    if spotcheck == "1":#finding what they played
        if board[1][1] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": #if blank  #replacing
            return True
    elif spotcheck == "2":#finding what they played
        if board[1][2] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": #if blank #replacing
            return True
    elif spotcheck == "3":#finding what they played
        if board[1][3] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": #if blank #replacing
            return True
    elif spotcheck == "4":#finding what they played
        if board[2][1] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": #if blank' #replacing
            return True
    elif spotcheck == "5":#finding what they played
        if board[2][2] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": #if blank #replacing
            return True
    elif spotcheck == "6":#finding what they played
        if board[2][3] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": #if blank #replacing
            return True
    elif spotcheck == "7":#finding what they played
        if board[3][1] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": #if blank #replacing
            return True
    elif spotcheck == "8":#finding what they played
        if board[3][2] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": #if blank #replacing
            return True
    elif spotcheck == "9":#finding what they played
        if board[3][3] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": #if blank #replacing
            return True
    else:
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
        player1_play = input("player "+ a +", what do you want to play: (_,_)  \n") # asking for input (_,_)
    elif a == '2': # checking whos playing 
        player2_play = input("player "+ a +", what do you want to play: (_,_)  \n") # asking for input (_,_)
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
    while game == True: #while loop
        if player_playing(board,'1') == True: # if player 1 played...
            if end(board,'x'): # end function to see if they won
                print ("player 1 wins!.... restarting\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
                main() # won 
            elif player_playing(board,'2') == True: # if didn't win then 
                if end(board,'o'): # end function to see if they won
                    print ("player 2 wins!.... restarting") # won
                    main() # won 
                gameloop(board) #LOOOOOOPPPPINGGGGGGG if no one won!
def main(): # main
    board = [[1,2,3],[4,5,6],[7,8,9]]  # making the board list so I can print it and replace in individual places
    print_board(board) # calling the print board function
    gameloop(board) # starting the game (player v player)
main()