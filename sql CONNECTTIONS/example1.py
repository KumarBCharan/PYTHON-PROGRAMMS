try:
    
    def connectionObject():
        import sqlite3
        conobj=sqlite3.Connection("Amma.db")
        return conobj
    conobj=connectionObject()
    def table_creation(conobj):
        curobj=conobj.cursor()
        curobj.execute('create table company(cname text,cgst int ,caddress text,cphone int)')
        conobj.commit()
    #table_creation(conobj)
    def insert_info(conobj):
        curobj=conobj.cursor()
        curobj.execute('insert into company values ("wipro",34567,"Hyderabadh",82172897727)')
        conobj.commit()
    #insert_info(conobj)
    def retrieve(conobj):
        curobj=conobj.cursor()
        data=curobj.execute('select *from company')
        for i in data:
            print(i)
    retrieve(conobj)
    def update(conobj):
        curobj=conobj.cursor()
        curobj.execute('update company set caddress="BGLR" where cgst=34567 ')
        conobj.commit()
    update(conobj)
    retrieve(conobj)
    def delete(conobj):
        curobj=conobj.cursor()
        curobj.execute('delete from company where cgst=34567')
        conobj.commit()
    delete(conobj)
    retrieve(conobj)
except Exception as e:
    print(e)
