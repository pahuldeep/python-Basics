import mysql.connector
from mysql.connector import Error
connection=mysql.connector.connect(host='localhost',user='root',password='********',database='pahuldb')

info=connection.get_server_info()
print(connection)
print(info)

sql = connection.cursor()

def create_database(db_name):
   query ='create database if not exists '+ db_name
   print(query)
   sql.execute(query)
create_database('pahuldb')

def create_table(tb_name):
   query = "create table if not exists " + tb_name + "(id int PRIMARY KEY, name VARCHAR(30), salary int, city VARCHAR(30))"
   print(query)
   sql.execute(query)
create_table("tb")

def insert_data(id,name,salary,city):
    query ="INSERT into tb(id,name,salary,city)"\
       "VALUES(%d,'%s',%d,'%s')"%\
       (id,name,salary,city)
    print(query)
    sql.execute(query)
    connection.commit()
    print(sql.rowcount,"data inserted sucessfully")
id=int(input('enter id: '));name=input('name: ');salary=int(input('enter salary: '));city=input('city: ')
insert_data(id,name,salary,city)

def fetchdata():
    sql.execute('SELECT * from tb')
    data=sql.fetchall()
    print(data[1][1]) # first row first column
    for i in data:
        print(i)
fetchdata()

print("update ur's data :")

def update_tb(name,city,salary,id):
    query="UPDATE tb SET name='%s',city='%s',salary='%s'"\
        "WHERE id='%s'"%\
        (name,city,salary,id)
    sql.execute(query)
    connection.commit()
    print("data updated")
#name=input('name: ');city=input('city: ');salary=int(input('enter salary: '));id=int(input('enter id: '))
#update_tb(name,city,salary,id)

def deletedata(id):
    query="DELETE from tb WHERE id = '%s'"%(id)
    sql.execute(query)
    connection.commit()
    print("data is deleted sucessfully")
    fetchdata()

#id=input("id :")
#deletedata(id)
#To comment on query --query--   LIMIT,WHERE,DISTICT,AND,OR,NOT,IN,BETWEEN,ORDER BY,GROUP BY,HAVING                
#SElECT*From tablename /WHERE city="CHD'LIMIT'"  
#SELECT distict(city) /From tablename 
#SELECT *From tablename /WHERE city='chd' AND salary=1000
#SELECT *From tablename /ORDER BY id DESC\ASC(asending,desending) LIMITS 5
#SELECT *From tablename /WHERE city in('CHD','mohali')
#sum(),avg(),min(),max(),count(),UNION,UNION ALL,JOINS
#SELECT sum(salary) From tablename
#SELECT count(id) From tablename
#SELECT sum(salary) From tablename/GROUPBY city(having condition)
#SELECT from tablename orderby salary desc limit 2
