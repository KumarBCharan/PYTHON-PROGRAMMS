import sqlite3
def connectionObject():
    con=sqlite3.connect('charan.db')
    return con
con=connectionObject()
def create_table(con):
    cro=con.cursor()
    cro.execute('create table student (sid integer primary key,sname text not null)')
    con.commit()
#create_table(con)
def insert_data(con):
    cro=con.cursor()
    cro.execute('insert into student values (52489,"aafiya")')
    con.commit()
#insert_data(con)
def retrieve_data(con):
    cro=con.cursor()
    query=cro.execute('select *from student')
    for i in query:
        print(i)
#retrieve_data(con)
def update_data(con):
    cro=con.cursor()
    cro.execute('update student set sname="FIYA" where sid=52489')
    con.commit()
#update_data(con)
#retrieve_data(con)
def delete_data(con):
    cro=con.cursor()
    cro.execute('delete from student where sid=25489')
    con.commit()

#delete_data(con)
#retrieve_data(con)
def alter_table(con):
    cro=con.cursor()
    cro.execute('alter table student add mobile text ')
    con.commit()
alter_table(con)
#retrieve_data(con)
def update_data(con):
    cro=con.cursor()
    cro.execute('update student set course="MSC PHYSICS" where sid=52489')
    con.commit() 
#update_data(con)
#retrieve_data(con)
def desc_table(con):
    cro=con.cursor()
    obj=cro.execute('pragma table_info(student)')
    for i in obj:
        print(i)
    row=cro.fetchall()
    for i in row:
        print(i)
    
    con.commit()
desc_table(con)
    
