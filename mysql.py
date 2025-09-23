import  pymysql

conn=pymysql.connect(
    host='localhost',
    user='root',
    password='Chaithra@2825',
    database='company')

cur=conn.cursor()

# sql="create table employee(id int primary key,name varchar(20))"
# sql="insert into employee values(1,'abu')"
# sql="insert into employee values(2,'anu')"
# sql="insert into employee values(3,'sachin')"
# sql="insert into employee values(4,'krish')"
# sql="insert into employee values(5,'madhu')"
sql="select * from employee"
cur.execute(sql)
#row=cur.fetchall()

#row=cur.fetchone()
#row=cur.fetchmany(2)
#print(row)

#for i in row:
    #print(i[0],i[1])


cur.execute(sql)

conn.commit()
conn.close()