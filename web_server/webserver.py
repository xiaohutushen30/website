#-*- coding: utf-8 -*
import web
import json

urls = (
    "/idcard$", "IdCard",
    "/personsn$", "PersonSN",
)
app = web.application(urls, globals()) # 绑定url
 
# 定义相应类
class IdCard:
    def GET(self):
        web.header('Content-Type', 'application/javascript;charset=utf-8')
        callback = web.input(callback='callback')['callback']
        result = json.dumps(self.get_card_info())
        return "%s(%s)" %(callback,result)

    def get_card_info(self):
        info = {
            "id_card":"685425542854669824",
            "name":u"张三",
            "sex":u"女"
        }
        return info

class PersonSN:
    def GET(self):
        web.header('Content-Type', 'application/javascript;charset=utf-8')
        callback = web.input(callback='callback')['callback']
        result = json.dumps(self.get_personsn())
        return "%s(%s)" %(callback,result)

    def get_personsn(self):
        info = {
            "personsn":"1111112222223333344444555555",
        }
        return info
 
if __name__ == "__main__":
    app.run()