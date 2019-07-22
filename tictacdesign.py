from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Tic Tac Toe")
global bclick
bclick=True

def close():
    exit()

def reset():
    button1["text"]=""
    button2["text"]=""
    button3["text"]=""
    button4["text"]=""
    button5["text"]=""
    button6["text"]=""
    button7["text"]=""
    button8["text"]=""
    button9["text"]=""


def winMethod():
         #code here to check win logic
         #delete pass
         pass
         reset()

def tictactoe(buttons):
    pass
    #code here to assign text
    #delete pass
    winMethod()



button1=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button1))
button1.grid(row=1,column=0)
button2=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button2))
button2.grid(row=1,column=1)
button3=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button3))
button3.grid(row=1,column=2)
button4=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button4))
button4.grid(row=2,column=0)
button5=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button5))
button5.grid(row=2,column=1)
button6=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button6))
button6.grid(row=2,column=2)
button7=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button7))
button7.grid(row=3,column=0)
button8=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button8))
button8.grid(row=3,column=1)
button9=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button9))
button9.grid(row=3,column=2)

button10=Button(root,text="Reset Game ",font=('Arial 9 bold'),height=1,width=6,command=reset)
button10.grid(row=4,column=0,columnspan=3,sticky=E+W)
button11=Button(root,text="Exit Game ",font=('Arial 9 bold'),height=1,width=6)
button11.grid(row=5,column=0,columnspan=3,sticky=S+N+E+W)

root.resizable(0,0)  # Dsabling WIndow Resize

root.mainloop()
