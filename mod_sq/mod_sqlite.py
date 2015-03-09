#coding:utf-8
import web

dbname = 'todos.db'
tname = 'todos'

db = web.database(dbn='sqlite', db=dbname)

class DB(object):
    @staticmethod
    def get_by_id(id):
        '''
        ret = dict(DB.get_by_id())
        '''
        done = 0
        itertodo = db.select(tname, where="id=$id", vars=locals())
        return next(iter(itertodo), None)

    @staticmethod
    def get_all():
        '''
        iter_item = DB.get_all()
        ret = []
        for item in iter_item:
            ret.append({
                "id": item.id,
                "title": item.title,
            })
        print ret
        #print json.dumps(ret)
        '''
        return db.select(tname)

    @staticmethod
    def create(**kwargs):
        db.insert(tname, **kwargs)

    @staticmethod
    def update(**kwargs):
        db.update(tname, where="id=$id", vars={"id": kwargs.pop('id')}, **kwargs)

    @staticmethod
    def delete(id):
        db.delete(tname, where="id=$id", vars=locals())
