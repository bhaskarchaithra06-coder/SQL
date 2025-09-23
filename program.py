import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='Chaithra@2825',
    database='company')
cur=conn.cursor()
#sql="create table department(id int primary key,name varchar(20))"
cur.execute(sql)
sql="insert into department values(301,'gokul')"
sql="insert into department values(302,'jiddu')"



conn.commit()
conn.close()
