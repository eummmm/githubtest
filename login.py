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
users=cur.fetchall()[0]
list02=[]
for item in users:
    list02.append(item)
user1 = input("请输入用户名")
while True:
    if user1 not in list02:
        user1=input("用户名输入错误")
    else:
        break
password1=input("请输入密码")
sss = "select password from register where user=(%s)"
cur.execute(sss,user1)
password=cur.fetchone()[0]
while True:
    if password!=password1:
        password1=("密码错误,请重新输入")
    else:
        print("登录成功")
        break





