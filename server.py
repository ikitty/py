#!/usr/bin/python
#coding:utf-8

import mm
import json
import web
import sqlite3
from mako.template import Template


conn = sqlite3.connect('data.db')
c = conn.cursor()

#create
#c.execute("CREATE TABLE category(id int primary key, name text)" )

#save changes
#conn.commit()

#insert
#c.execute("INSERT INTO category VALUES (1, 'test book')");
#c.execute("INSERT INTO category VALUES (?, ?)", (2, 'test2'));

#insert list
books = [(3, 'book3'),
        (4, 'book4'),
        ]

#c.executemany("INSERT INTO category VALUES (?,?)", books)

c.execute("SELECT * FROM category")
#fetchone : get one data
print(c.fetchall())
#c.execute("SELECT * FROM category WHERE id=3")

c.execute("UPDATE category SET name = 'test modify' WHERE id = 3")
c.execute("SELECT * FROM category")
print(c.fetchall())


#delete one data
c.execute("DELETE FROM category WHERE id = 4")
c.execute("SELECT * FROM category")
print(c.fetchall())

conn.commit()
conn.close()


urls = (
    '/', 'index',
    '/test/', 'Test',
    '/bblib/(.*)', 'source',
)

class index:
    def GET(self):
        t = Template(filename='test.html', input_encoding='utf-8')
        return t.render()

class source:
    #如果urls中有匹配字符，这里必须写形参。否则会报错
    def GET(self, fname):
        return mm.rfile('bblib/' + fname)


class Test:
    def GET(self):
        return json.dumps({"name":"jack", "age": 10})

    def POST(self):
        data = web.data()
        print data
        return "success"

    def DELETE(self):
        data = web.data()
        print data
        return "delete success"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
