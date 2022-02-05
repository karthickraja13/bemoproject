from tabulate import tabulate
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
mycursor=conn.cursor()

mycursor.execute("SELECT * FROM file")

result=mycursor.fetchall()

for x in result:
    print(tabulate(result, headers=["id", "name", "password"]))
conn.commit()
conn.close()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
mycursor=conn.cursor()

mycursor.execute("UPDATE file SET name='raja' ,password='123'  WHERE id=4")
print(mycursor.rowcount)
conn.commit()
conn.close()



conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
mycursor=conn.cursor()
data="INSERT INTO  file (name, password) VALUES (%s, %s)"
val=("ram",123)
mycursor.execute(data,val)
print("insert successfully")

conn.commit()
conn.close()



conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
mycursor=conn.cursor()
sql="DELETE FROM file WHERE id=8"
mycursor.execute(sql)
print("delete")
conn.commit()
conn.close()

