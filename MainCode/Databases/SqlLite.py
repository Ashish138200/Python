import sqlite3 

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id NUMBER,name TEXT)")
    conn.commit()
    conn.close

def insert_data(id,name):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES(?,?)",(id,name))
    conn.commit()
    conn.close

#insert_data(2,'Arpit')

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows
print(view())

def delete(id):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,)) #extra comma is mandatory
    conn.commit()
    conn.close()

def update(name):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET name=? WHERE id=2", (name,))  # extra comma is mandatory
    conn.commit()
    conn.close()

insert_data(2,'Arpit')
print(view())
update('Mansi')
print(view())
delete(2)
print(view())