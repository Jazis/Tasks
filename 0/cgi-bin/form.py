# coding: utf-8
import pymysql
import pymysql.cursors
import threading
import cgi

def db_query(text):
    print("Content-type: text/html\n")
    try:
        connection = pymysql.connect(host='127.0.0.1',
                                    user='hahs',
                                    password='147147Zxc',
                                    db='db_something',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        try:
            for i in range(20):
                try:
                    with connection.cursor() as cursor:
                        # insert  =  INSERT INTO `db_something`.`stable` (`rubrics`, `text`, `created_date`) VALUES ('rub0', 'Something text, i thing. Search word - hello', 'yesterday')
                        sql = "SELECT * FROM `{0}`.`{1}` WHERE `text` LIKE '%{2}%' ORDER BY text LIMIT 1 OFFSET {3}".format('db_something', 'stable', text, i)
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        print(rows)
                    connection.commit()
                except:
                    pass
        finally:
            connection.close()
    except pymysql.err.OperationalError:
        print("Sql error")

if __name__ == "__main__":
    form = cgi.FieldStorage()
    text1 = form.getfirst("file_text", "")
    s = text1
    b = s.encode("UTF-8")
    db_query(b)