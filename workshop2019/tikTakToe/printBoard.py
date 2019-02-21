

def printBoard(theBoard):
    boardTop = f"{theBoard['top-L']} | {theBoard['top-M']} |{theBoard['top-R']}"
    boardMid = f"{theBoard['mid-L']} | {theBoard['mid-M']} |{theBoard['mid-R']} "
    boardLow = f"{theBoard['low-L']} | {theBoard['low-M']} |{theBoard['low-R']} "
    print(boardTop)
    print('-+--+-')
    print(boardMid)
    print("-+--+-")
    print(boardLow)
