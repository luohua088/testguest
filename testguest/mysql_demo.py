from pymysql import cursors,connect

#连接数据库
conn = connect(host = '127.0.0.1',
               user = 'root',
               password = '123456',
               db = 'testguest',
               charset = 'utf8mb4',
               cursorsclass = cursors.DictCursor)

try:
    with conn.cursor() as cursors:
        #创建嘉宾数据
        sql = 'INSERT INTO sign_guest (realname,phone,email,sign,event_id,cerate_time)' \
              ' VALUE ("tom",18800010002,"tom@11.com",0,1,NOW());'
        cursors.execute(sql)
        #提交事务
        conn.commit()

    with conn.cursor() as cursors:
        #查询添加的嘉宾
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone = %s"
        cursors.execute(sql,('18800010002',))
        result = cursors.fetchone()
        print(result)

finally:
    conn.close()



