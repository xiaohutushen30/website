#-*- coding: utf-8 -*
import web
 
urls = ("/.*", "hello")        # 指定任何url都指向hello类
app = web.application(urls, globals()) # 绑定url
 
# 定义相应类
class hello:
    def GET(self):
        return 'Hello, world!'
 
if __name__ == "__main__":
    app.run()