# -*- coding: utf-8 -*-
'''
WEB应用的本质：
1、浏览器发送一个HTTP请求
2、服务器收到请求后，生成一个HTML文档
3、服务器把HTML文档作为http响应的body发送给浏览器
4、浏览器收到HTTP响应，从httpbody取出html文档并显示
'''
from wsgiref.simple_server import make_server


def application(environ, start_response):
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'WEB')
    return [body.encode("utf-8")]


httpd = make_server("", 8000, application)
print("Server on HTTP on port 8000...")
httpd.serve_forever()

