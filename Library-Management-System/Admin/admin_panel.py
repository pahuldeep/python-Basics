from tkinter import *
import datetime as dt
from tkinter import messagebox
from issue_book import issue
from add_book import *
from return_book import return_book

#INSERT INTO `issued_books` VALUES ('3', '1', CURRENT_DATE(), \
        #(SELECT DATE_ADD("2017-06-15", INTERVAL 20 DAY)))

#def disp():
#    frame=Frame(root1)
#    img=PhotoImage(file='bg.png')
#    label=Label(frame,image=img)
#    label.pack()
#    frame.pack()
#    root1.after(2000,admin)
#    root1.mainloop()
#    root1.destroy()
    

def admin():
    #root1.destroy()
    root=Tk()
    root.title('Admin Panel')
    root.geometry('400x500')
    frame1=Frame(root,height=100)
    label=Label(frame1,text=' Welcome Admin ',bg='orange',fg='white',relief=SUNKEN,\
                font=('comic sans ms',18,'bold')).pack()
    frame1.pack(fill=X,pady=50)

    frame1=Frame(root,height=100)
    bt1=Button(frame1,text='Add Book',font=('Verdana',15,'bold'),\
               command=lambda : add_book(root)).pack()
    frame1.pack(fill=X,pady=10)

    frame1=Frame(root,height=100)
    bt1=Button(frame1,text='Issue Book',font=('Verdana',15,'bold'),\
               command=lambda: issue(root)).pack()
    frame1.pack(fill=X,pady=10)

    frame1=Frame(root,height=100)
    bt1=Button(frame1,text='Return Book',font=('Verdana',15,'bold'),\
               command=lambda:return_book(root)).pack()
    frame1.pack(fill=X,pady=10)

    root.mainloop()


if __name__=='__main__':
    import admin_login

