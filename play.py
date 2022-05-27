from Board import Board
from AI import AI
import time

if __name__ == '__main__' :
    board = Board(5,5,4)
    board.display()
    ai = AI(2, board)
    

    n = 0

    while(board.checkWin()== 'none'):
        if n % 2 != 0:
            coor = ai.analysis()
            value = 'x'
        else:
            text = input("Enter i,j of o: ") # 0,0
            coor = [int(i) for i in text.split(",")] # [1,0]
            value = 'o'    
        if not (board.put(coor[0],coor[1],value)):
            print("error to put i,j")
        else: 
            board.display()
            print("--------------------------")
            n += 1
    if board.checkWin() == 'draw':
        print("draw")
    else:
        print(f"winner is {board.checkWin()}")