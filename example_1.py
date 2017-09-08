#! /usr/bin/python
#-*- coding: utf-8 -*-

from flask import Flask  #从flask框架导入Flask类
from flask.config import Config
app = Flask(__name__)     #实例化一个后台对象
class CONFIG:
    DEBUG = True
# app.config.from_json('config.json')
# app.config.from_pyfile('config.py')
# app.config.from_object(CONFIG)
# app.config.update(DEBUG=True)
# app.config['DEBUG'] = True
print(app.config)

#app.route('/')           #也可实现函数和路径的绑定
#app.route必须调用了以后，才是一个装饰器
@app.route('/')
def hello_world():             #定义一个页面
    return '<h1>Hello world!</h1>'
#app.add_url_rule('/',view_func=index)    #绑定后台对象规则，调用后台方法，让路径和函数对应起来，一个路径对应一个函数
# def func(f):
#     def wrapper(*args,**kwargs):
#         print('运行了函数')
#         return f(*args,**kwargs)
#     return wrapper
# @app.route('/')
# @func
# def fccc():
#     return 'xxxx'
if __name__ == '__main__':
    app.run()                               #启动后台
