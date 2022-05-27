import numpy as np
class Board:
    def __init__(self,m, n, a):
        self.board = np.zeros([m,n], dtype=int)
        self.a = a

    def indexOfA(self, i, j):
         #ไปทางขวา
        r = []
        for k in range(self.a):
            if j+k < self.board.shape[1]:
                r.append([i, j+k])
        
        #ลงข้างล่าง
        b = []
        for k in range(self.a):
            if i+k < self.board.shape[0]:
                b.append([i+k, j])
        
        #ขวาล่าง
        rb = []
        for k in range(self.a):
            if i+k < self.board.shape[0] and j+k < self.board.shape[1]:
                rb.append([i+k, j+k])
        
        lb = []
        for k in range(self.a):
            if i+k < self.board.shape[0] and j-k >= 0:
                lb.append([i+k, j-k])

        array_out = []
        if len(r) == self.a: array_out.append(r)
        if len(b) == self.a: array_out.append(b)
        if len(rb) == self.a: array_out.append(rb)
        if len(lb) == self.a: array_out.append(lb)

        return array_out
    def checkWin(self):
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                array_out = self.indexOfA(i,j)
                for k in range(len(array_out)):
                    count_x = 0
                    count_o = 0
                    for coor in array_out[k]:
                        if self.board[coor[0], coor[1]] == 1:
                            count_o +=1
                        if self.board[coor[0], coor[1]] == 2:
                            count_x +=1
                    if count_x == self.a : return 'x'
                    if count_o == self.a : return 'o'
        if self.checkDraw():
            return 'draw'
        else:
            return 'none'


    def put(self, i, j, value):
        try:
            if self.board[i,j] != 0:
                return False
            else:
                if value == "o":
                    self.board[i,j] = 1
                    return True
                elif value == "x":
                    self.board[i,j] = 2
                    return True
                else:
                    return False
        except:
            return False
    
    def display(self):
        for i in range(np.shape(self.board)[0]):
            for j in range(np.shape(self.board)[1]):
                if j == 0:
                    print("|",end="")
                if self.board[i,j] == 0:
                    print(f"  ", end=" |")
                elif self.board[i,j] == 1:
                    print(f" o", end=" |")
                elif self.board[i,j] == 2:
                    print(f" x", end=" |")
                if j == np.shape(self.board)[1] - 1:
                    print("\n")
    
    def checkDraw(self):
        for i in range(np.shape(self.board)[0]):
            for j in range(np.shape(self.board)[1]):
                if self.board[i,j] == 0:
                    return False
        return True

