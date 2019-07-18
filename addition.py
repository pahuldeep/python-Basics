import tkinter as t 
root = t.Tk()
root.title("Addition")
root.geometry("800x400")

lable1=t.Label(root,text="value :")
lable1.grid(padx=10,pady=10,row=0,column=0)

textbox1=t.Entry(root)
textbox1.grid(row=0,column=1)

lable2=t.Label(root,text="value :")
lable2.grid(padx=10,pady=10,row=1,column=0)

textbox2=t.Entry(root)
textbox2.grid(row=1,column=1)

def calc():
    a=textbox1.get()
    b=textbox2.get()
    c=int(a)+int(b)
    textbox3.insert(0,c)

lable3=t.Label(root,text="result :")
lable3.grid(padx=10,pady=10,row=2,column=0)

textbox3=t.Entry(root)
textbox3.grid(row=2,column=1)

button=t.Button(root,text="sum",command=calc)
button.grid(row=3,column=1)


root.mainloop()
