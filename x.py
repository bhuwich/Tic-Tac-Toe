import socket
from cProfile import label
from email.mime import image
from Board import Board
import tkinter as tk
from AI import AI
import easygui 
from tkinter import *
from easygui import *
import tkinter.messagebox
import threading
root = tk.Tk()
root.iconbitmap("tic_tac_toe.ico")
root.title("Tic Tac Toe Game : X Player")
root.resizable(False,False)
board = Board(5,5,4)
play = True
ai = AI(2, board)


x = PhotoImage(file="xplayer.png")
o = PhotoImage(file="oplayer.png")
def play():
    button1 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,0,True))
    button1.grid(row=0,column=0)

    button2 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,1,True))
    button2.grid(row=0,column=1)

    button3 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,2,True))
    button3.grid(row=0,column=2)

    button4 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,3,True))
    button4.grid(row=0,column=3)

    button5 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(0,4,True))
    button5.grid(row=0,column=4)

    button6 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,0,True))
    button6.grid(row=1,column=0)

    button7 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,1,True))
    button7.grid(row=1,column=1)

    button8 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,2,True))
    button8.grid(row=1,column=2)

    button9 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,3,True))
    button9.grid(row=1,column=3)

    button10 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(1,4,True))
    button10.grid(row=1,column=4)

    button11 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,0,True))
    button11.grid(row=2,column=0)

    button12 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,1,True))
    button12.grid(row=2,column=1)

    button13 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,2,True))
    button13.grid(row=2,column=2)

    button14 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,3,True))
    button14.grid(row=2,column=3)

    button15 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(2,4,True))
    button15.grid(row=2,column=4)

    button16 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,0,True))
    button16.grid(row=3,column=0)

    button17 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,1,True))
    button17.grid(row=3,column=1)

    button18 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,2,True))
    button18.grid(row=3,column=2)

    button19 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,3,True))
    button19.grid(row=3,column=3)

    button20 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#cc99ff',command=lambda:press(3,4,True))
    button20.grid(row=3,column=4)

    button21 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,0,True))
    button21.grid(row=4,column=0)

    button22 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,1,True))
    button22.grid(row=4,column=1)

    button23 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,2,True))
    button23.grid(row=4,column=2)

    button24 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,3,True))
    button24.grid(row=4,column=3)

    button25 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#bf80ff',command=lambda:press(4,4,True))
    button25.grid(row=4,column=4)
    
def press(r,c,Turn): 
    global play,TCP_IP,TCP_PORT,BUFFER_SIZE,message
    if Turn:
        labelPhoto = Label(root,image = x)
        labelPhoto.grid(row=r,column=c)  
        send(r,c)       
        board.put(r,c,"x")
    if Turn == False:
        labelPhoto = Label(root,image = o)
        labelPhoto.grid(row=r,column=c)         
        board.put(r,c,"o")
  
    if(board.checkWin()!= 'none'):
        if board.checkWin() == 'draw':
            msgbox("Draw T-T")                          
        else:
            msgbox("Winner is "+board.checkWin()+"!!!!!!!!","Winner","close") 
def server():
    global TCP_IP,TCP_PORT,BUFFER_SIZE,conn,s
    while True: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP,TCP_PORT))
        data = s.recv(BUFFER_SIZE).decode("utf-8")
        press(int(data[:1]),int(data[-1:]),False)

        s.close()
def send(r,c):
    message = str(r)+","+str(c)  
    s.sendall(message.encode('utf-8'))

TCP_IP = "127.0.0.1"
TCP_PORT = 8081
BUFFER_SIZE = 1024  

threading.Thread(target = play).start()
threading.Thread(target = server).start()


root.mainloop()
