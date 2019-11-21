from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox

def return_to_admin(root):
    root.destroy()
    from admin_panel import admin
    admin()

    
def add_book(root_admin):

    racks=[*range(1,51)]
    root_admin.destroy()
    root=Tk()
    root.title('Add Book')
    root.geometry('600x600')
    
    frame1=Frame(root,height=100)
    bt=Button(frame1,text='HOME',font=('cambria',10,'underline'))
    bt.grid(row=0,column=0,padx=60)
    
    frame1=Frame(root,height=100)
    bt=Button(frame1,text='HOME',font=('cambria',10,'underline'),command=lambda:return_to_admin(root))
    bt.grid(row=0,column=0,padx=60)
    label=Label(frame1,text=' Add Book ',bg='orange',fg='white',relief=SUNKEN,font=('comic sans ms',18,'bold'))
    label.grid(row=0,column=1,padx=70)
    frame1.pack(fill=X,pady=40)
    
    root2=Frame(root,width=120,height=50)
    label2=Label(root2,text='Book title : ',font=('Verdana',12,'bold'))
    label2.grid(row=0,column=0)

    entry1=Entry(root2,font=('Verdana',12))
    entry1.grid(row=0,column=1)
    root2.pack(fill=X,pady=12,padx=100)


    #
    test_root=Frame(root,width=120,height=50)
    labelk=Label(test_root,text='keywords : ',font=('Verdana',12,'bold'))
    labelk.grid(row=0,column=0)

    keyword=Entry(test_root,font=('Verdana',12))
    keyword.grid(row=0,column=1)
    test_root.pack(fill=X,pady=12,padx=100)
    #
    root3=Frame(root,width=120,height=120)
    label3=Label(root3,text='Author : ',font=('Verdana',12,'bold'))
    label3.grid(row=0,column=0)

    entry2=Entry(root3,font=('Verdana',12))
    entry2.grid(row=0,column=1)
    root3.pack(fill=X,pady=12,padx=122)

    #
    root2=Frame(root,width=120,height=50)
    label2=Label(root2,text='Publisher : ',font=('Verdana',12,'bold'))
    label2.grid(row=0,column=0)

    entry3=Entry(root2,font=('Verdana',12))
    entry3.grid(row=0,column=1)
    root2.pack(fill=X,pady=12,padx=100)

    #
    root3=Frame(root,width=120,height=120)
    label3=Label(root3,text='Edition : ',font=('Verdana',12,'bold'))
    label3.grid(row=0,column=0)

    entry4=Entry(root3,font=('Verdana',12))
    entry4.grid(row=0,column=1)
    root3.pack(fill=X,pady=12,padx=122)

    root2=Frame(root,width=120,height=50)
    label2=Label(root2,text='Total Pages : ',font=('Verdana',12,'bold'))
    label2.grid(row=0,column=0)

    entry5=Entry(root2,font=('Verdana',12))
    entry5.grid(row=0,column=1)
    root2.pack(fill=X,pady=12,padx=78)

    #
    root3=Frame(root,width=120,height=120)
    label3=Label(root3,text='Block : ',font=('Verdana',12,'bold'))
    label3.grid(row=0,column=0)

    drop=ttk.Combobox(root3,values=['A','B','C','D'])
    drop.current(0)
    drop.grid(row=0,column=1)
    root3.pack(fill=X,pady=12,padx=137)

    #
    root2=Frame(root,width=120,height=50)
    label2=Label(root2,text='Rack number : ',font=('Verdana',12,'bold'))
    label2.grid(row=0,column=0)

    drop=ttk.Combobox(root2,values=racks)
    drop.current(0)
    drop.grid(row=0,column=1)
    root2.pack(fill=X,pady=12,padx=68)

    
    def insert_book():
        db=sql.connect(host='localhost',user='root',passwd='pahul1999',db='library')
        cursor=db.cursor()

        book=entry1.get()
        book=book.capitalize()
    
        pub=entry3.get()
        pub=pub.capitalize()
    
        aut=entry2.get()
        aut=aut.capitalize()
    
        rack=entry4.get()
        
        pages=entry5.get()
        
        block=drop.get()
    
        keywords=keyword.get()
        keywords=keywords.capitalize()
    
        rack=rack.capitalize()+'-'+block
        code='PUP-'+book[:3].upper()+str(pages)
        issued=0

        query="insert into book_details values('{}','{}','{}','{}',{},'{}','{}','{}')".format(code,book,aut,pub,int(pages),rack,issued,keywords)
        cursor.execute(query)
        db.commit()
        db.close()

    root2=Frame(root,width=120,height=50)
    bt=Button(root2,text='Add in database',font=('Comic sans ms',16,'bold'),bd=4,command=insert_book)
    bt.pack()
    root2.pack(pady=30)
    root.mainloop()

if __name__=='__main__':
    import admin_login
