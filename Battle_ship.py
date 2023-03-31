import random
from playsound import playsound
def random_shots(player_board,computer_hit):
    shotx = random.randint(1,5)
    shoty = random.randint(1,5)
    if player_board[shotx][shoty] == ' 💥':
        random_shots(player_board,computer_hit)
    if player_board[shotx][shoty] == ' 🛥️ ':
        print("computer HIT!")
        player_board[shotx][shoty] = ' 💥' 
        computer_hit = computer_hit +1
    else:
        player_board[shotx][shoty] = ' 💦'
    return [computer_hit]

def random_ship():
    boaty = random.randint(1,5)
    boatx = random.randint(1,5)
    return [boatx,boaty]
def printboard(board):
    line = ""
    for i in board:
        line = ""
        for j in i: # this makes it so that it makes it print the board in a grid
            #print new row 
            line = line + j + " "
        print(line)
def computer_ship_function(computer_board):
    random_ships = random_ship()
    boatx = random_ships[0]
    boaty = random_ships [1]
    if boaty <= 1 or boaty >= 5:
        return False
    if boatx <= 1 or boatx >= 5:
        return False
    else:
        if computer_board[boatx][boaty] == ' 🛥️ ':
            return False
        else: 
            computer_board[boatx][boaty] = ' 🛥️ '
            return computer_board
def random_board_switching(computer_board,loop):
    check = computer_ship_function(computer_board)
    if check == False:
        random_board_switching(computer_board,loop)
    else:
        loop = loop +1
        board = check
        if loop <= 5:
            random_board_switching(computer_board,loop)
        if loop > 5:
            printboard(board)
def user_playing(player_board,board):
    player_boat_placement = input("where do you want to put your boats (row,col)")
    player_boat_placement = player_boat_placement.split(",")
    try:
        player_boat_placement_row = int(player_boat_placement[0])
        player_boat_placement_col = int(player_boat_placement[1])
    except:
        print("wrong input")
        user_playing(player_board,board)
    try:
        if player_board[player_boat_placement_row][player_boat_placement_col] == ' 🛥️ ':
            print("                                          alrighty placed a boat there bud ")
            user_playing(player_board,board)
        else:
            player_board[player_boat_placement_row][player_boat_placement_col] = ' 🛥️ '
            printboard(player_board)
            board = board + 1
            if board <= 5:
                user_playing(player_board,board)
            if board > 5:
                quit
    except:
        print("wrong input")
        user_playing(player_board,board)
def computer_shooting(player_board,computer_hits):
    random_shots(player_board,computer_hits)
    return computer_hits
def player_shooting(computer_board,player_attack_board,hit):
    try:
        shot = input("where would you like to shoot? (row,col)")
        shot = shot.split(",")
        shotx = int(shot[0])
        shoty = int(shot[1])
        if computer_board[shotx][shoty] == ' 💥':
            print("you alrighty exploded that")
            player_shooting(computer_board,player_attack_board,hit)
        if computer_board[shotx][shoty] == ' 💦':
            print("you alrighty missed there buddy")
            player_shooting(computer_board,player_attack_board,hit)
        if computer_board[shotx][shoty] == ' 🛥️ ':
            print("93 YOU HIT!")
            player_attack_board[shotx][shoty] = ' 💥'
            hit = hit +1
            playsound(r'C:\Users\cjenkins24\Documents\GitHub\Comp-Sci\explotion.wav')
        else:
            if computer_board[shotx -1][shoty-1] == ' 🛥️ ':
                print("you were close to hitting")
            if computer_board[shotx][shoty-1] == ' 🛥️ ':
                print("you were close to hitting")
            if computer_board[shotx +1][shoty-1] == ' 🛥️ ':
                print("you were close to hitting")
            if computer_board[shotx-1][shoty] == ' 🛥️ ':
                print("you were close to hitting")
            if computer_board[shotx][shoty] == ' 🛥️ ':
                print("you were close to hitting")
            if computer_board[shotx+1][shoty] == ' 🛥️ ':
                print("you were close to hitting")
            if computer_board[shotx-1][shoty+1] == ' 🛥️ ':
                print("you were close to hitting")
            if computer_board[shotx][shoty+1] == ' 🛥️ ':
                print("you were close to hitting")
            if computer_board[shotx+1][shoty+1] == ' 🛥️ ':
                print("you were close to hitting")
            player_attack_board[shotx][shoty] = ' 💦'
            playsound(r'C:\Users\cjenkins24\Documents\GitHub\Comp-Sci\splash.wav')
        return [hit]
    except:
        print("wrong input.... try again")
        player_shooting(computer_board,player_attack_board,hit)
def game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits):
    computer_hits = computer_shooting(player_board,computer_hits)
    print("computer is done shooting")
    player_hit = player_shooting(computer_board,player_attack_board,player_hit)
    if computer_hits == 5:
        print("computer won \n\n\n\n\n\n\n\n")
    if player_hit == 5:
        print("you won \n\n\n\n\n\n\n\n\n\n")
        main()
    else:
        return [player_hit,computer_hits]
def big_game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits):
    game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits)
    printboard(player_attack_board)
    boardprint = input("would you like to see where the computer shot? (their shooting board), (yes or no)\n")
    if boardprint == 'yes':
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        printboard(player_board)
    boardprint = input("continue? ENTER")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    printboard(player_attack_board)
    big_game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits)
def main():
    player_attack_board = [["   1 "," 2 "," 3 "," 4 "," 5 "],["1"," 0 "," 0 "," 0 "," 0 "," 0 "],["2"," 0 "," 0 "," 0 "," 0 "," 0 "],["3"," 0 "," 0 "," 0 "," 0 "," 0 "],["4"," 0 "," 0 "," 0 "," 0 "," 0 "],["5"," 0 "," 0 "," 0 "," 0 "," 0 "]]
    player_board = [["   1 "," 2 "," 3 "," 4 "," 5 "],["1"," - "," - "," - "," - "," - "],["2"," - "," - "," - "," - "," - "],["3"," - "," - "," - "," - "," - "],["4"," - "," - "," - "," - "," - "],["5"," - "," - "," - "," - "," - "]]
    computer_attack_board = [["   1 "," 2 "," 3 "," 4 "," 5 "],["1"," 0 "," 0 "," 0 "," 0 "," 0 "],["2"," 0 "," 0 "," 0 "," 0 "," 0 "],["3"," 0 "," 0 "," 0 "," 0 "," 0 "],["4"," 0 "," 0 "," 0 "," 0 "," 0 "],["5"," 0 "," 0 "," 0 "," 0 "," 0 "]]
    computer_board = [[" " ," 1 "," 2 "," 3 "," 4 "," 5 "],["1"," - "," - "," - "," - "," - "],["2"," - "," - "," - "," - "," - "],["3"," - "," - "," - "," - "," - "],["4"," - "," - "," - "," - "," - "],["5"," - "," - "," - "," - "," - "]]
    #printboard(player_attack_board)
    #printboard(player_board)
    loop = 1
    random_board_switching(computer_board,loop)
    board = 1
    printboard(player_board)
    user_playing(player_board,board)
    print("you have finished your placing")
    player_hit = 0
    computer_hits = 0
    big_game_loop(player_board,computer_board,player_attack_board,player_hit,computer_hits)
main()