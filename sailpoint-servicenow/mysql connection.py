import mysql.connector

def insertData(con,cur,name,id):
    cur.execute(f"INSERT INTO employee (name,id) VALUES ('{name}',{id});")
    con.commit()

def displayAllData(con,cur,table):
    cur.execute(f"select * from {table};")
    rows = cur.fetchall()
    for r in rows:
        print(f'Name : {r[0]} , ID : {r[1]}')


con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Pass@123",
    database = "testing",
    port = 3306
)

cur = con.cursor()

name ="python1"
id = 777

insertData(con,cur,name,id)
displayAllData(con,cur,'employee')

con.close()