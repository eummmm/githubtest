import pymysql

db=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="login",
    charset="utf8"
    )
cur=db.cursor()


sql="select user from register"
cur.execute(sql)
users=cur.fetchall()
list01=[]
for item in users:
    list01.append(item)
while True:
    while True:
        user=input("请输入用户名")
        if user not in list01:
            break
    password=input("请输入密码")
    sss="insert into register (user,password) values (%s,%s)"
    cur.execute(sss,[user,password])
    db.commit()









