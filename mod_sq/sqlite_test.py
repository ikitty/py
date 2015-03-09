#!/usr/bin/python
#coding:utf-8
#sqlite操作测试

import json
import web
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS category (id int primary key, name text)" )

#save changes
#conn.commit()

c.execute("INSERT INTO category VALUES (1, 'test book')");
c.execute("INSERT INTO category VALUES (?, ?)", (2, 'test2'));

#insert list
#books = [(3, 'book3'), (4, 'book4'), ]
#c.executemany("INSERT INTO category VALUES (?,?)", books)

c.execute("SELECT * FROM category")
print(c.fetchall())
#c.execute("SELECT * FROM category WHERE id=3")

#c.execute("UPDATE category SET name = 'test modify' WHERE id = 3")
#c.execute("SELECT * FROM category")
#print(c.fetchall())

#delete one data
#c.execute("DELETE FROM category WHERE id = 4")
#c.execute("SELECT * FROM category")
#print(c.fetchall())

#conn.commit()
conn.close()
