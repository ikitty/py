#!/usr/bin/python
#coding:utf-8

import json

from mod_sqlite import DB

testcase = 2

if testcase == 1:
    ret = {}
    dbret = DB.get_by_id(1)
    for item in dbret:
        ret[item] = dbret[item]
    print ret

    #print dict(DB.get_by_id(1))

if testcase == 2 :

    iter_item = DB.get_all()
    ret = []
    for item in iter_item:
        ret.append({
            "id": item.id,
            "title": item.title,
        })
    print ret
    #print json.dumps(ret)

if testcase == 3 :
    data = {
        'title': "test create"
        ,'done':1
    }
    DB.create(**data)

if testcase == 4 :
    data = {
        'id':1
        ,'title': "test modify"
    }

    DB.update(**data)

if testcase == 5 :

    DB.delete(2)
