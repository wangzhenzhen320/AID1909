"""
insert update delete
"""
import pymysql

#连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user = 'root',
                     password='123456',
                     database='stu',
                     charset='utf8')
#生成游标对象（用于操作数据库数据，获取sql执行结果的对象）
cur = db.cursor()

#对数据库执行写操作
try:
    #insert插入
    #age=input("age")
    #score=input("score")
    #sql = "insert into myclass (name,age,score) values (%s,%s,%s);"
    #cur.execute(sql,[name,age,score])
    #update 操作
    #sql = "update myclass set sex='m' where name='Bill';"
    #cur.execute(sql)
    #delete 删除
    #sql = "delete from myclass where sex is null;"
    #cur.execute(sql)

    #同时执行多次sql语句
    exe = []
    for i in range(3):
        name=input("name")
        age=input("age")
        score=input("score")
        exe.append((name,age,score))
    sql = "insert into myclass (name,age,score) values (%s,%s,%s);"
    cur.executemany(sql,exe)

    db.commit() #同步写操作
except Exception as e:
    print(e)
    db.rollback() #出错时数据库恢复到之前的状态

#关闭游标和数据库
cur.close()
db.close()
