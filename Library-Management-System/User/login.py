from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
import time
from main import panel

localtime = time.asctime( time.localtime(time.time()) )
localtime=localtime.split()
x=localtime[1]+' '+localtime[2]+', '+localtime[-1]
localtime.pop(1)
localtime.pop(1)
localtime.pop(-1)
localtime.insert(1,x)
x=localtime[2][:5]
localtime.pop(-1)
localtime.insert(2,x)
localtime=', '.join(localtime)

root=Tk()
root.configure(bd=4,relief=SOLID)
root.title('Login Window')
root.geometry('700x500')

def close_win():
    root.destroy()

def neww():
    newwin=Toplevel(root)

def login():
    db=sql.connect(host='localhost',user='root',passwd='pahul1999',db='library')
    cursor=db.cursor()
    
    user_id=entry1.get()
    user_id=user_id.lower()
    pass1=entry2.get()

    try:
        query="select user_id,password from user_details where user_id='{}'".format(user_id)
        cursor.execute(query)
        pass2=cursor.fetchone()
        user_id=pass2[0]
        pass2=pass2[1]

        
        if pass1==pass2:
            query="insert into user_login_details VALUES ('{}',NOW())".format(user_id)
            cursor.execute(query)
            db.commit()
            db.close()
            root.destroy()
            panel()
        elif pass1!=pass2:
            messagebox.showinfo('Alert Box','Login Credentials not matched!!')
    except:
        messagebox.showinfo('Alert Box','Error!!')
        

root1=Frame(root,width=100,height=100)
label1=Label(root1,text=' Login into Library ',bg='purple',fg='white',font=('Comic sans',15,'bold'),relief=SUNKEN,height=2,width=18,bd=4)
label1.pack()
label1=Label(root1,text='\n'+localtime,font=('Comic sans',15))
label1.pack()
root1.pack(fill=X,pady=80)

root2=Frame(root,width=100,height=50)
label2=Label(root2,text='Username : ',font=('Verdana',12,'bold'))
label2.pack(side=LEFT)

entry1=Entry(root2,font=('Verdana',12),bd=2)
entry1.pack(side=LEFT)
root2.pack(fill=X,padx=190)

root3=Frame(root,width=100,height=100)
label3=Label(root3,text='Password : ',font=('Verdana',12,'bold'))
label3.pack(side=LEFT)

entry2=Entry(root3,font=('Verdana',12),bd=2)
entry2.pack(side=LEFT)
root3.pack(fill=X,pady=15,padx=194)

root4=Frame(root,width=100,height=100,bd=4)
submit=Button(root4,text='Login',font=('Verdana',12,'bold'),command=login,bg='yellow',fg='black',width=5)
submit.grid(row=0,column=0)
submit=Button(root4,text='Exit',font=('Verdana',12,'bold'),bg='blue',fg='white',width=5,command=close_win)
submit.grid(row=0,column=3,padx=50)
root4.pack(fill=X,pady=20,padx=250)

root.mainloop()
