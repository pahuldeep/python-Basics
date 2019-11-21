def books(lab1,lab2='',lab3='',lab4='',radio=0):

    import mysql.connector as sql

    lab1=lab1.capitalize()
    lab2=lab2.capitalize()
    lab3=lab3.capitalize()
    lab4=lab4.capitalize()

    db=sql.connect(host='localhost',user='root',passwd='pahul1999',db='library')
    cursor=db.cursor()
    query="select book_name,author,publisher,rack,issued from book_details where book_name like '{}%' ".format(lab1)
    
    if (lab2=='' and lab3=='' and lab4==''):
        query=query+"order by book_name"

    elif (lab2!='' and lab3=='' and lab4==''):
        query=query+"and author like '{}%' order by book_name".format(lab2)

    elif (lab2!='' and lab3!='' and lab4==''):
        query=query+"and author like '{}%' and publisher like '{}%' order by book_name".format(lab2,lab3)

    elif (lab2=='' and lab3!='' and lab4!=''):
        query=query+"and publisher like '{}%' and keywords like '{}%' order by book_name".format(lab3,lab4)

    elif (lab2!='' and lab3!='' and lab4!=''):
        query=query+"and author like '{}%' and publisher like '{}%' and keywords like '{}%' order by book_name".format(lab2,lab3,lab4)
        
    
    if radio==1:
        query=query+" and author"
        
    elif radio==2:
        query=query+" and publisher"
        
    elif radio==3:
        query=query+" and issued"


    cursor.execute(query)
    data=cursor.fetchall()
    cursor.close()
    db.close()
        
    return data

if __name__=='__main__':
    import login
