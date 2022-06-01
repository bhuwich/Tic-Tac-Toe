import numpy as np
class AI:
    def __init__(self, value, board):
        self.value = value
        self.board = board

    def calXOb(self, board, value):
        XOb =0
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                array_out = self.board.indexOfA(i,j)
                for k in range(len(array_out)):
                    count_x = 0
                    count_o = 0
                    for coor in array_out[k]:
                        if board[coor[0], coor[1]] == 1:
                            count_o +=1
                        if board[coor[0], coor[1]] == 2:
                            count_x +=1
                    if value == 'o' and count_x == 0:
                        XOb += count_o
                    if value == 'x' and count_o ==0:
                        XOb += count_x
        return XOb
    def analysisLose(self):# ใช้สำหรับป้องกันการชนะ ใช้เป็นอันดับสองก่อนจะคำนวน vb ด้วยซ้ำ
        board = self.board.board
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                array_out = self.board.indexOfA(i,j)
                for k in range(len(array_out)):
                    count_ = 0
                    count_empty = 0
                    for coor in array_out[k]:
                        if board[coor[0], coor[1]] != self.value and board[coor[0], coor[1]] !=0:
                            count_ += 1
                        if board[coor[0], coor[1]] == 0:
                            count_empty +=1
                    if count_ == self.board.a-1 and count_empty ==1:
                        for coor in array_out[k]:
                            if board[coor[0], coor[1]] == 0:
                                return coor

                
    def analysisWin(self):# ใช้สำหรับการชนะก่อน ใช้เป็นอันดับแลกก่อนจะคำนวน vb
        board = self.board.board
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                array_out = self.board.indexOfA(i,j)
                for k in range(len(array_out)):
                    count_ = 0
                    count_empty = 0
                    for coor in array_out[k]:
                        if board[coor[0], coor[1]] == self.value:
                            count_ += 1
                        if board[coor[0], coor[1]] == 0:
                            count_empty +=1
                    if count_ == self.board.a-1 and count_empty ==1:
                        for coor in array_out[k]:
                            if board[coor[0], coor[1]] == 0:
                                return coor
                    

    def analysis(self):
        coor_win = self.analysisWin()
        coor_lose = self.analysisLose()
        if coor_win is not None : return coor_win
        if coor_lose is not None : return coor_lose
        board_tmp = np.array(self.board.board) # copy board
        vb_table = -30*np.ones(np.shape(board_tmp))

        # try to put
        for i in range(np.shape(board_tmp)[0]):
            for j in range(np.shape(board_tmp)[1]):
                if board_tmp[i,j] == 0:
                    board_tmp[i,j] = self.value #ลองวาง
                    if self.value == 1:
                        vb_table[i,j] = self.calXOb(board_tmp, 'o') - self.calXOb(board_tmp, 'x') 
                    else:
                        vb_table[i,j] = self.calXOb(board_tmp, 'x') - self.calXOb(board_tmp, 'o')
                    board_tmp[i,j] = 0 #เอาออก              
        vb_max = np.max(vb_table)
        for i in range(np.shape(vb_table)[0]):
            for j in range(np.shape(vb_table)[1]):
                if vb_table[i,j] == vb_max:
                    return [i,j]