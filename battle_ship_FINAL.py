'''
created on Sep 12, 2022
Description: user plays battle ship agaist a computer (1v1)

Last edited: 1/23/2023
bugs: paramiters
@AUTHOR: Charlie Jenkins
'''
import random                                         # importing random
from playsound import playsound                       # importing the sound
def random_shots(player_board,computer_hit):          # defining function
    shotx = random.randint(1,5)                       # x random 
    shoty = random.randint(1,5)                       # y random
    if player_board[shotx][shoty] == ' 💥':           # checking if the point hit, run the function
        random_shots(player_board,computer_hit)       # function  for running it again making a loop
    elif player_board[shotx][shoty] == ' 🛥️ ':        # if there is a boat there then it is a hit
        print("computer HIT!")                        # printing for user
        player_board[shotx][shoty] = ' 💥'            #changing the board
        computer_hit = computer_hit +1                # looping 
    else:                                             # else
        player_board[shotx][shoty] = ' 💦'            # changing the board
    return [computer_hit]                             # returning the output

def random_ship():                                    # function (placing the boats)
    boaty = random.randint(1,5)                       # random y
    boatx = random.randint(1,5)                       # random x
    return [boatx,boaty]                              # returning cord.

def printboard(board):                                # function (building the board)
    line = ""                                         #building the board
    for i in board:                                   # layering
        line = ""
        for j in i:                                   # this makes it so that it makes it print the board in a grid
            line = line + j + " "
        print(line)
def computer_ship_function(computer_board):           # defining function
    random_ships = random_ship()                      # varible = function
    boatx = random_ships[0]                           # random x
    boaty = random_ships [1]                          # random y
    if boaty <= 1 or boaty >= 5:                      # making sure it is in the board
        return False                                  # braking
    elif boatx <= 1 or boatx >= 5:                    # same
        return False                                  # same
    else:                                             # if it is....
        if computer_board[boatx][boaty] == ' 🛥️ ':   # checking if it alrighty placed
            return False            
        else: 
            computer_board[boatx][boaty] = ' 🛥️ '     # changing it to a boat
            return computer_board                       # returning
def random_board_switching(computer_board,loop):        # defining a function
    check = computer_ship_function(computer_board)      # checking...
    if check == False:                                  # braking 
        random_board_switching(computer_board,loop)     # running function (loop)
    else:                                               # else...
        loop = loop +1                                  #loop counter
        board = check                                   # changing varible
        if loop <= 5:                                   # checking amount of loops
            random_board_switching(computer_board,loop) # looping...
        if loop > 5:                                    # checking amount of loops
            printboard(board)                           # printing the board
def user_playing(player_board,board):                   # function defining
    player_boat_placement = input("where do you want to put your boats (row,col)")      # placing user board (asking)
    player_boat_placement = player_boat_placement.split(",")   # splitting by comma
    paramiter=("bad")                  
    try:                                                                                # trying (inside board)
        player_boat_placement_row = int(player_boat_placement[0])                       # varibles for row and collom from the split
        player_boat_placement_col = int(player_boat_placement[1]) 
        if player_boat_placement_col > 0 and player_boat_placement_col <= 5:
            paramiter=("good")
        if player_boat_placement_row > 0 and player_boat_placement_row <= 5:
            paramiter=("good")
        else: 
            user_playing(player_board,board)
    except:
        print("wrong input")                                                            # bullet proofing
        user_playing(player_board,board)                                                #looping if wrong
    try:                                                                                # trying (checking if brakes)
        if player_board[player_boat_placement_row][player_boat_placement_col] == ' 🛥️ ':        # checking if they alrighty played there
            print("                                          alrighty placed a boat there bud ")  # printing to help user understand (sorry)
            user_playing(player_board,board)                                                        # giving them another try
        else:
            player_board[player_boat_placement_row][player_boat_placement_col] = ' 🛥️ '            #making 
            printboard(player_board)                              # printing board
            board = board + 1                                     # loop counter
            if board <= 5:      
                user_playing(player_board,board)            # calling
            if board > 5:
                quit()                                        # braking
    except:
        print("wrong input")                                    # bullet proofing
        user_playing(player_board,board)
def computer_shooting(player_board,computer_hits):          # calling function
    random_shots(player_board,computer_hits)                # calling function within function
    return computer_hits                                    # returning
def player_shooting(computer_board,player_attack_board,hit):   #shooting...
    try:
        shot = input("where would you like to shoot? (row,col)")            # asking
        shot = shot.split(",") # splitting
        shotx = int(shot[0])                                                # x input
        shoty = int(shot[1])                                                # y input
        if computer_board[shotx][shoty] == ' 💥':                           # checking
            print("you alrighty exploded that")                             # printing
            player_shooting(computer_board,player_attack_board,hit)         #looping
        elif computer_board[shotx][shoty] == ' 💦':                         #checking 
            print("you alrighty missed there buddy")                        # printing
            player_shooting(computer_board,player_attack_board,hit)         # looping
        elif computer_board[shotx][shoty] == ' 🛥️ ':                        # checking 
            print("YOU HIT!")                                               #priting YOU HIT
            player_attack_board[shotx][shoty] = ' 💥'                       #  changing
            hit = hit +1                                                    # loop counter
            playsound(r'C:\Users\cjenkins24\Documents\GitHub\Comp-Sci\explotion.wav') # playing sound (has to be inside the folder)
        else:                                                           # helping the user to know if they were close
            if computer_board[shotx -1][shoty-1] == ' 🛥️ ':            # telling them they were close               
                print("you were close to hitting")
            elif computer_board[shotx][shoty-1] == ' 🛥️ ':            # telling them they were close
                print("you were close to hitting")
            elif computer_board[shotx +1][shoty-1] == ' 🛥️ ':            # telling them they were close
                print("you were close to hitting")
            elif computer_board[shotx-1][shoty] == ' 🛥️ ':            # telling them they were close
                print("you were close to hitting")
            elif computer_board[shotx][shoty] == ' 🛥️ ':            # telling them they were close
                print("you were close to hitting")
            elif computer_board[shotx+1][shoty] == ' 🛥️ ':            # telling them they were close
                print("you were close to hitting")
            elif computer_board[shotx-1][shoty+1] == ' 🛥️ ':            # telling them they were close
                print("you were close to hitting")
            elif computer_board[shotx][shoty+1] == ' 🛥️ ':            # telling them they were close
                print("you were close to hitting")
            elif computer_board[shotx+1][shoty+1] == ' 🛥️ ':            # telling them they were close
                print("you were close to hitting")
            player_attack_board[shotx][shoty] = ' 💦'            # changing it to the splash so they know they missed on the board
            playsound(r'C:\Users\cjenkins24\Documents\GitHub\Comp-Sci\splash.wav') #playing sound (has to be inside the folder)
        return [hit]                                            # returning
    except:                                 # bullet profing
        print("wrong input.... try again")
        player_shooting(computer_board,player_attack_board,hit)
def game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits):   # looping the game (checking whos winning)
    computer_hits = computer_shooting(player_board,computer_hits)                           # calling the computer function 
    print("computer is done shooting")                                                      # step 1 done
    player_hit = player_shooting(computer_board,player_attack_board,player_hit)                 # player shooting
    if computer_hits == 5:                                                                  # checking whos won
        print("computer won \n\n\n\n\n\n\n\n")                                              # printing
    elif player_hit == 5:                                                                 # checking whos won
        print("you won \n\n\n\n\n\n\n\n\n\n")                                               # printing
        main()                                                                                  # looping to play again
    else:
        return [player_hit,computer_hits]                                                   # returning
def big_game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits):                # big game loop function
    game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits)                     # calling smaller loop
    printboard(player_attack_board)                                                                          #  after round printing board
    boardprint = input("would you like to see where the computer shot? (their shooting board), (yes or no)\n")  # seeing if they want to see where the computer hit (new board)
    if boardprint == 'yes':                                                                                     # checking their answer
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")                                                                     # new lines
        printboard(player_board)                                                                                #printing
    boardprint = input("continue? ENTER")                                                                       # seeing when they want to continue
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")                                                         # new lines
    printboard(player_attack_board)                                                                                     # printing board
    big_game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits)                     #looping
def main():                                                                                                 #MAIN                                                                                                                                   all of these board are for different things (name explains them)
    player_attack_board = [["   1 "," 2 "," 3 "," 4 "," 5 "],["1"," 0 "," 0 "," 0 "," 0 "," 0 "],["2"," 0 "," 0 "," 0 "," 0 "," 0 "],["3"," 0 "," 0 "," 0 "," 0 "," 0 "],["4"," 0 "," 0 "," 0 "," 0 "," 0 "],["5"," 0 "," 0 "," 0 "," 0 "," 0 "]]   #board
    player_board = [["   1 "," 2 "," 3 "," 4 "," 5 "],["1"," - "," - "," - "," - "," - "],["2"," - "," - "," - "," - "," - "],["3"," - "," - "," - "," - "," - "],["4"," - "," - "," - "," - "," - "],["5"," - "," - "," - "," - "," - "]]          #another board
    computer_attack_board = [["   1 "," 2 "," 3 "," 4 "," 5 "],["1"," 0 "," 0 "," 0 "," 0 "," 0 "],["2"," 0 "," 0 "," 0 "," 0 "," 0 "],["3"," 0 "," 0 "," 0 "," 0 "," 0 "],["4"," 0 "," 0 "," 0 "," 0 "," 0 "],["5"," 0 "," 0 "," 0 "," 0 "," 0 "]] # another another board
    computer_board = [[" " ," 1 "," 2 "," 3 "," 4 "," 5 "],["1"," - "," - "," - "," - "," - "],["2"," - "," - "," - "," - "," - "],["3"," - "," - "," - "," - "," - "],["4"," - "," - "," - "," - "," - "],["5"," - "," - "," - "," - "," - "]]     # another another another board
    loop = 1 # looping
    random_board_switching(computer_board,loop)# running function 
    board = 1 # looping
    printboard(player_board) # calling for the first print
    user_playing(player_board,board) # calling the user function
    print("you have finished your placing") # first round
    player_hit = 0
    computer_hits = 0
    big_game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits)  # calling big loop
main() # calling the first main