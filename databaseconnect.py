from pymysql import *

conn=connect(host="localhost",user='root',db='buddha')
print("Conection established")
mycusrsor=conn.cursor()


# query="create table student_info(name varchar(50),email varchar(60))"
# mycusrsor.execute(query)
# print("table created successfully")

# queins="insert into student_info(name,email) " \
#        "values('ashwwani','a@gmail.com')"
# mycusrsor.execute(queins)


# a='mera'
# b='mera@gmail.com'
# queins="insert into student_info(name,email) " \
#         "values(%s,%s)"
# value = (a,b)
# mycusrsor.execute(queins,value)
# conn.commit() #to save the data permamnently
# print("data inserted successfully")

fetch_data="select * from student_info"
mycusrsor.execute(fetch_data)
result=mycusrsor.fetchall()
print(result)
final_result = [list(i) for i in result]

print(final_result)