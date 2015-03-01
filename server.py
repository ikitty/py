#!/usr/bin/python
# coding:utf-8

import mm
import json
import web
from mako.template import Template

urls = (
    '/', 'index',
    '/man/', 'Man',
    '/boy/', 'Boy',
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

class Boy:
    def GET(self):
        return json.dumps({"name":"boyJack", "age": 10})


class Man:
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
