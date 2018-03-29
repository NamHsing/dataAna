#coding=utf-8
from snownlp import SnowNLP
import pymysql
import numpy

con=pymysql.connect(host='123.206.45.78', port=3306, user='sa', passwd='sail1989', db='test', charset='utf8')
cur = con.cursor()
sqlsen = "select * from wbc"
try:
    cur.execute(sqlsen)
    for row in cur.fetchall():
        text=row[1]
        svalue=SnowNLP(text)
        #text=text.encode('utf-8')
        sqltemp="update wbc set sens=%d where content='%s'"
        cur.execute(sqltemp %(svalue.sentiments,text))
        print text
        print(svalue.sentiments)

    cur.close()
except Exception as e:
    raise e

con.close()

