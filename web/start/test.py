# -*- coding: UTF-8 -*-
import web

# URL 规则
urls = (
    '/wei', 'hello'
)

# 应用程序
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name: name = 'world'
        web.header('Content-Type', 'text/html; charset=UTF-8')
        return '你好，' + '世界' + '！'

# 启动
if __name__ == "__main__":
    app.run()