from printBoard import printBoard


def takeIpAndDisplay(theBoard):
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)

        if turn == 'X':
            ip = input("X move:")
            theBoard[ip] = 'x'
            turn = '0'
        else:
            ip = input("0 move:")
            theBoard[ip] = 'o'
            turn = 'X'
