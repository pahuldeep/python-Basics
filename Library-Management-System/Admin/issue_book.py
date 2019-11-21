from tkinter import *
import datetime as dt
import mysql.connector as sql
from tkinter import messagebox

today=dt.datetime.now()

def return_to_admin(root):
    root.destroy()
    from admin_panel import admin
    admin()

def insert_data(sid,code,issue,return_date):
    book_id=code.get()
    user_id=sid.get()
    issue_date=issue.get()
    return_dat=return_date.get()
    
    if book_id=='' or user_id=='':
        messagebox.showinfo('Alert','Insert some values!!')
        return
    try:
        db=sql.connect(host='localhost',user='root',passwd='pahul1999',db='library')
        cursor=db.cursor()

        query="select book_details.book_code,user_details.user_id from book_details inner join user_details where book_code='{}' and user_id='{}';".format(book_id,user_id)
        cursor.execute(query)
        result=cursor.fetchone()
        print(result)

        if result==None:
            messagebox.showinfo('Alert','Book not found!!')
            db.close()
            return
        else:
            query="insert into issued_books(user_id,book_code,issued_on,return_date) values('{}' ,'{}' ,'{}' ,'{}')".format(user_id,book_id,issue_date,return_dat)
            cursor.execute(query)
            qry="UPDATE book_details SET issued = issued+1 WHERE book_code='{}'".format(book_id)
            cursor.execute(qry)
            db.commit()
            db.close()
    except:
        messagebox.showinfo('Alert','Book not found!!!!')
        
def issue(root1):
    root1.destroy()
    root=Tk()
    root.title('Issue Book')
    root.geometry('600x600')

    frame1=Frame(root,height=100)
    bt=Button(frame1,text='HOME',font=('cambria',10,'underline'),command=lambda:return_to_admin(root))
    bt.grid(row=0,column=0,padx=60)
    
    label=Label(frame1,text=' Issue Book ',bg='orange',fg='white',relief=SUNKEN,font=('comic sans ms',18,'bold'))
    label.grid(row=0,column=1,padx=70)
    frame1.pack(fill=X,pady=40)

    #book-code
    frame1=Frame(root,height=100)
    label=Label(frame1,text='Book code : ',font=('verdana',12))
    label.pack(side=LEFT)
 
    code=Entry(frame1,font=('verdana',12))
    code.pack(side=LEFT)

    frame1.pack(fill=X,padx=120,pady=40)

    #student-id
    frame1=Frame(root,height=100)
    label=Label(frame1,text='Student ID : ',font=('verdana',12))
    label.pack(side=LEFT)
    sid=Entry(frame1,font=('verdana',12))
    sid.pack(side=LEFT)
    frame1.pack(fill=X,padx=115)

    frame1=Frame(root,height=100)
    label=Label(frame1,text='Issue Date : ',font=('verdana',12))
    label.pack(side=LEFT)
    issue=Entry(frame1,font=('verdana',12))
    issue.insert(0,today.strftime('%d/%m/%y'))
    issue.pack(side=LEFT)
    frame1.pack(fill=X,padx=115,pady=40)

    frame1=Frame(root,height=100)
    label=Label(frame1,text='Return Date : ',font=('verdana',12))
    label.pack(side=LEFT)
    return_date=Entry(frame1,font=('verdana',12))
    return_date.insert(0,(today+dt.timedelta(days=15)).strftime('%d/%m/%y'))
    return_date.pack(side=LEFT)
    frame1.pack(fill=X,padx=105)

    frame1=Frame(root,height=100)
    bt=Button(frame1,text='Issue',font=('cambria',16,'bold'),bd=5,width=10,command=lambda:insert_data(sid,code,issue,return_date))
    bt.pack()
    frame1.pack(fill=X,padx=105,pady=50)

if __name__=='__main__':
    import admin_login

