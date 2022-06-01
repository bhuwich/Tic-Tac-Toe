from ast import arg
from multiprocessing.sharedctypes import Value
import socket
import threading
from cProfile import label
from email.mime import image
from Board import Board
import tkinter as tk
from AI import AI
import easygui 
from tkinter import *
from easygui import *
import tkinter.messagebox

root = tk.Tk()
root.iconbitmap("tic_tac_toe.ico")
root.title("Tic Tac Toe Game : O Player")
root.resizable(False,False)
board = Board(5,5,4)
TCP_IP = "127.0.0.1"
TCP_PORT = 8081
BUFFER_SIZE = 1024
turnPlay = True
ai = AI(2, board)
x = PhotoImage(file="xplayer.png")
o = PhotoImage(file="oplayer.png")
def play():
    button1 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,0))
    button1.grid(row=0,column=0)

    button2 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,1))
    button2.grid(row=0,column=1)

    button3 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,2))
    button3.grid(row=0,column=2)

    button4 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,3))
    button4.grid(row=0,column=3)

    button5 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,4))
    button5.grid(row=0,column=4)

    button6 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,0))
    button6.grid(row=1,column=0)

    button7 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,1))
    button7.grid(row=1,column=1)

    button8 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,2))
    button8.grid(row=1,column=2)

    button9 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,3))
    button9.grid(row=1,column=3)

    button10 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,4))
    button10.grid(row=1,column=4)

    button11 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,0))
    button11.grid(row=2,column=0)

    button12 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,1))
    button12.grid(row=2,column=1)

    button13 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,2))
    button13.grid(row=2,column=2)

    button14 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,3))
    button14.grid(row=2,column=3)

    button15 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,4))
    button15.grid(row=2,column=4)

    button16 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,0))
    button16.grid(row=3,column=0)

    button17 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,1))
    button17.grid(row=3,column=1)

    button18 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,2))
    button18.grid(row=3,column=2)

    button19 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,3))
    button19.grid(row=3,column=3)

    button20 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,4))
    button20.grid(row=3,column=4)

    button21 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,0))
    button21.grid(row=4,column=0)

    button22 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,1))
    button22.grid(row=4,column=1)

    button23 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,2))
    button23.grid(row=4,column=2)

    button24 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,3))
    button24.grid(row=4,column=3)

    button25 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,4))
    button25.grid(row=4,column=4)
    
def press(r,c): 
    global turnPlay,o
    if turnPlay:
        labelPhoto = Label(root,image = o)
        labelPhoto.grid(row=r,column=c)
        board.put(r,c,"o")
        message = str(r)+","+str(c)  
        conn.sendall(message.encode('utf-8'))
        turnPlay = False
    if turnPlay == False:  
        rev()
        turnPlay = True

    if(board.checkWin()!= 'none'):
        if board.checkWin() == 'draw':
            msgbox("Draw T-T")                          
        else:
            msgbox("Winner is "+board.checkWin()+"!!!!!!!!","Winner","close") 

def server():
    global TCP_IP,TCP_PORT,BUFFER_SIZE,conn
    while True: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP,TCP_PORT)) 
        s.listen(5)
        conn, addr = s.accept()
        
        s.close()

        

def rev():
    global x
    data = conn.recv(BUFFER_SIZE)  
    data = data.decode("utf-8")
    labelPhoto = Label(root,image = x)
    labelPhoto.grid(row=int(data[:1]),column=int(data[-1:]))
    board.put(int(data[:1]),int(data[-1:]),"x")
    
threading.Thread(target = play).start()
threading.Thread(target = server).start()


root.mainloop()