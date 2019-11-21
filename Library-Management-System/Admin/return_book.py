from tkinter import *
import datetime as dt
from tkinter import messagebox
import mysql.connector as sql

today=dt.datetime.now()

def return_to_admin(root):
    root.destroy()
    from admin_panel import admin
    admin()
    
def update_database(book_code,return_date):
    no=0
    code=book_code
    return_date=dt.datetime.strptime(return_date.get(),"%d/%m/%y")
    book_code=book_code.get()
    book_code=book_code.lower()

    db=sql.connect(host='localhost',user='root',passwd='pahul1999',db='library')
    cursor=db.cursor()
    
    query="select return_date from issued_books where book_code='{}'".format(book_code)
    cursor.execute(query)
    result=cursor.fetchone()
    if result==None:
        messagebox.showinfo('Alert!','Book not found!!')
        db.close()
        code.delete(0,END)
        return
    else:
        expected_date=result[0]
        expected_date=dt.datetime.strptime(expected_date,"%d/%m/%y")
        delta=return_date-expected_date
        delta=delta.days
        query="update book_details set issued={} where book_code='{}'".format(no,book_code)
        cursor.execute(query)
        #db.commit()
        query="delete from issued_books where book_code='{}'".format(book_code)
        cursor.execute(query)
        #db.commit()
        db.close()
        messagebox.showinfo('Alert!','Book returned!!\n\nFine = '+str(delta)+' ₹')
        code.delete(0,'end')
        return
   

def return_book(root):
    root.destroy()
    root=Tk()
    root.title('Return Book')
    root.geometry('600x600')

    frame1=Frame(root,height=100)
    bt=Button(frame1,text='HOME',\
                font=('cambria',10,'underline'),\
              command=lambda:return_to_admin(root))
    bt.grid(row=0,column=0,padx=60)

    label=Label(frame1,text=' Return Book ',bg='orange',fg='white',relief=SUNKEN,\
                font=('comic sans ms',18,'bold'))
    label.grid(row=0,column=1,padx=70)
    frame1.pack(fill=X,pady=40)

    frame1=Frame(root,height=100)
    label=Label(frame1,text='Book code : ',\
                font=('verdana',12))
    label.pack(side=LEFT)

    code=Entry(frame1,\
                font=('verdana',12),bd=2)
    code.pack(side=LEFT)
    frame1.pack(fill=X,padx=120,pady=30)

    frame1=Frame(root,height=100)
    label=Label(frame1,text='Return Date : ',\
                font=('verdana',12))
    label.pack(side=LEFT)
    issue=Entry(frame1,\
                font=('verdana',12),bd=2)
    issue.insert(0,today.strftime('%d/%m/%y'))
    issue.pack(side=LEFT)
    frame1.pack(fill=X,padx=105)

    frame1=Frame(root,height=100)
    bt=Button(frame1,text='Return Book',\
                font=('cambria',16,'bold'),bd=5,width=12,\
              command=lambda:update_database(code,issue))
    bt.pack()
    frame1.pack(fill=X,padx=105,pady=50)
    
    root.mainloop()
    
if __name__=='__main__':
    import admin_login
