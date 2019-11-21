from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from get_book import books

def destroy(root_login):
    root_login.destroy()

def panel():   
    root1=Tk()

    root=Frame(root1)
    root1.title('Library Management')
    root1.geometry('800x600')

    label1=Label(root,text='Book name : ',font=('Verdana',12))
    label1.grid(row=0,column=0,pady=10)

    entry1=Entry(root,font=('Verdana',12),bd=2)
    entry1.grid(row=0,column=1,pady=10)

    label2=Label(root,text='Author name : ',font=('Verdana',12))
    label2.grid(row=1,column=0)

    entry2=Entry(root,font=('Verdana',12),bd=2)
    entry2.grid(row=1,column=1,pady=8)

    label3=Label(root,text='Publisher : ',font=('Verdana',12))
    label3.grid(row=0,column=2,pady=10,padx=15)

    entry3=Entry(root,font=('Verdana',12),bd=2)
    entry3.grid(row=0,column=3,pady=10)

    label4=Label(root,text='Keywords : ',font=('Verdana',12))
    label4.grid(row=1,column=2,pady=10,padx=15)

    entry4=Entry(root,font=('Verdana',12),bd=2)
    entry4.grid(row=1,column=3,pady=10)
    root.pack(pady=10)

    label5=Label(root,text='Sort by : ',font=('Comic Sans',10,'bold italic'))
    label5.grid(row=2,column=0,pady=10,padx=15)

    var=IntVar()
    r1 = Radiobutton(root, text='Author',font=('Comic Sans',10,'bold'), variable=var,value=1)
    r1.grid(row=2, column=1)

    r2 = Radiobutton(root, text='Publsiher',font=('Comic Sans',10,'bold'), variable=var,value=2)
    r2.grid(row=2, column=2)

    r3 = Radiobutton(root, text='Issued',font=('Comic Sans',10,'bold'), variable=var,value=3)
    r3.grid(row=2, column=3)

    #textarea
    frame1=Frame(root1)
    text=tkst.ScrolledText(master = frame1,width  = 67,height = 20,font=('Verdana',11))
    text.grid(row=0,column=1)
    frame1.pack(expand = YES,padx=15)
    
    def disp(x):
        headings=('| S.no |','| Book Name |','| Author |','| Publisher |','| Rack  |','| Issued |')
        text.insert(INSERT,headings)
        for i in x:
            if i==x[0] or i==x[-1] or i==x[-2]:
                text.insert(INSERT,[i])
            else:
                text.insert(INSERT,i+' '*15)
    
    def get_values():
        words = text.get(1.0,END)
        if words:
            text.delete(1.0,END)
        lab1=entry1.get()
        if lab1=='':
            messagebox.showinfo('Alert!','Book name is required')
            return
        lab2=entry2.get()
        lab3=entry3.get()
        lab4=entry4.get()
        var1=var.get()
        data=books(lab1,lab2,lab3,lab4,var1)
        disp(data)
    #submit
    submit=Button(root,text='List Books',bd=3,font=('Cambria',12,'bold'),
                  command=get_values)
    submit.grid(row=3,columnspan=4,pady=10)

    root.mainloop()

if __name__=='__main__':
    import login