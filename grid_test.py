def printboard(board):
    print('1 2 3 4 5 6')
    for x in range(5):
        for i in range(6):
            print(board[i][4-x],end = " ")
        print('')
def main():
    board = [[' x ',' o ',' o ',' o ',' o ',' o '],[' x ',' o ',' o ',' o ',' o ',' o '],[' x ',' o ',' o ',' o ',' o ',' o '],[' x ',' o ',' o ',' o ',' o ',' o '],[' x ',' o ',' o ',' o ',' o ',' o '],[' x ',' o ',' o ',' o ',' o ',' o '],[' x ',' o ',' o ',' o ',' o ',' o ']]
    printboard(board)
main()