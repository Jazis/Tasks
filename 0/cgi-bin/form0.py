# coding: utf-8
import pymysql
import pymysql.cursors
import threading
import cgi

def db_query(text):
    print("Content-type: text/html\n")
    try:
        connection = pymysql.connect(host='127.0.0.1',
                                    user='me',
                                    password='mepass',
                                    db='db_something',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM `{0}`.`{1}` WHERE `id` = {2}".format('db_something', 'stable', text)
                cursor.execute(sql)
                rows = cursor.fetchall()
                connection.commit()
                print("Item by id '{0}' deleted".format(text))
        finally:
            connection.close()
    except pymysql.err.OperationalError:
        print("Sql error")

if __name__ == "__main__":
    form = cgi.FieldStorage()
    text1 = form.getfirst("file_text", "")
    db_query(text1)