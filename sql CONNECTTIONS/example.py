def connection_object():
    import sqlite3
    conobj=sqlite3.Connection("charan.db")
    return conobj
conobj=connection_object()
def create_table(conobj):
     curobj=conobj.cursor()
     curobj.execute('create table emp(empid int , ename text)')
     conobj.commit()
     print("table is created successfully")
#create_table(conobj)
def insert_date(conobj):
    curobj=conobj.cursor()
    curobj.execute('insert into emp values(150150,"ammu")')
    conobj.commit()
    print("inserted successfully")
#insert_date(conobj)
def retriev_data(conobj):
    curobj=conobj.cursor()
    queryset=curobj.execute('select *from emp')
    for i in queryset:
        print(i)
    
    print("retrieving data successfully")
retriev_data(conobj)
def update_data(conobj):
    curobj=conobj.cursor()
    curobj.execute('update  emp set ename="physics faculty" where empid=15')
    conobj.commit()
    print("updating the data successfully")
update_data(conobj)
def delete_data(conobj):
    curobj=conobj.cursor()
    curobj.execute('delete from emp where empid=150150')
    conobj.commit()
    print("deleted the data successfully")
delete_data(conobj)
retriev_data(conobj)
