#coding:utf-8

import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

try:
    cur.execute('CREATE TABLE IF NOT EXISTS test (id integer PRIMARY KEY AUTOINCREMENT, title text,done boolean default False);')
    con.commit()
except Exception as e:
    print e
cur.execute('INSERT INTO test(title,  done) values("明天下午3点,coding",  0);')
con.commit()

cur.close()
con.close()
