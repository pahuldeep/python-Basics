import mysql.connector
con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="*********",
                            database="pahuldb")
sql=con.cursor()
import tkinter as t
root = t.Tk()

root.title("registration form")
root.geometry("600x400")

t.Label(root,text="Name :").grid(padx=10,pady=10,row=0,column=0)
Name=t.Entry(root)
Name.grid(row=0,column=1)

t.Label(root,text="City :").grid(padx=10,pady=10,row=1,column=0)
City=t.Entry(root)
City.grid(row=1,column=1)

t.Label(root,text="Mobile no :").grid(padx=10,pady=10,row=2,column=0)
Mobile_no=t.Entry(root)
Mobile_no.grid(row=2,column=1)

t.Label(root,text="Email :").grid(padx=10,pady=10,row=3,column=0)
Email=t.Entry(root)
Email.grid(row=3,column=1)

t.Label(root,text="password :").grid(padx=10,pady=10,row=4,column=0)
Password=t.Entry(root,show="*")
Password.grid(row=4,column=1)

t.Label(root,text="Choose Gender :").grid(padx=10,row=5,column=0)
v = t.IntVar()
t.Radiobutton(root,text="male",variable=v,value=1).grid(padx=10,row=5,column=1)
t.Radiobutton(root,text="female",variable=v,value=2).grid(padx=10,row=5,column=2)
   
t.Label(root,text="choose Language:").grid(padx=10,row=6,column=0)
v1=t.IntVar();v2=t.IntVar();v3=t.IntVar()
t.Checkbutton(root,text="php",variable=v1).grid(padx=10,row=6,column=1)
t.Checkbutton(root,text="java",variable=v2).grid(padx=10,row=6,column=2)
t.Checkbutton(root,text="python",variable=v3).grid(padx=10,row=6,column=3)
def gender():
    if v.get() == 1:
        g="male"
    else:
        g="female"
    return g
def course():
    if v1.get() == 1 and v2.get() == 1 and v3.get() == 1:
        c="php,java,python"
    elif v1.get() == 1 and v2.get() == 1 and v3.get() == 0:
        c="php,java"
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0:
        c="php"
    elif v1.get() == 0 and v2.get() == 1 and v3.get() == 1:
        c="java,phython"
    elif v1.get() == 0 and v2.get() == 0 and v3.get() == 1:
        c="python"
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 1:
        c="php,python"
    elif v1.get() == 0 and v2.get() == 0 and v3.get() == 0:
        c="None"
    return c
def submit():
     print("Done.......")
     n=Name.get()
     C=City.get()
     m=Mobile_no.get()
     e=Email.get()
     p=Password.get()
     g = gender()
     c = course()
     query ="INSERT into register(name,city,mobile,email,password,gender,course)"\
         "VALUES('%s','%s','%s','%s','%s','%s','%s')"%\
         (n,C,m,e,p,g,c)
     sql.execute(query)
     con.commit()
t.Button(root,text="Register",command=submit).grid(padx=20,pady=20,row=7,column=2)
root.mainloop()
