#-*- coding: utf-8 -*
import web
import json
import serial 
import string 
import binascii 

urls = (
    "/idcard$", "IdCard",
    "/personsn$", "PersonSN",
)
app = web.application(urls, globals()) # 绑定url

def hexShow(argv):  
    result = ''  
    hLen = len(argv)  
    for i in xrange(hLen):  
        hvol = ord(argv[i])  
        hhex = '%02x'%hvol  
        result += hhex+' '  
    print 'hexShow:',result 
    return result

def get_personsn():
    t = serial.Serial('com20',115200,timeout = 1)  
    print t.portstr  
    #strInput = raw_input('enter some words:') 
    strInput = "\xff\x04\x06\x00\x01\xc2\x00\xa4\x60"
    n = t.write(strInput)  
    print n  
    str = t.read(50)  
    print str
    hexShow(str)
    str_line = "----------------------------------------------"
    print str_line

    strInput = "\xff\x00\x04\x1d\x0b"
    n = t.write(strInput)  
    print n
    str = t.read(50)  
    print str  
    hexShow(str)
    str_line = "----------------------------------------------"
    print str_line

    strInput = "\xff\x02\x93\x00\x05\x51\x7d"
    n = t.write(strInput)  
    print n  
    str = t.read(50)  
    print str
    hexShow(str)
    str_line = "----------------------------------------------"
    print str_line

    strInput = "\xff\x01\x97\x06\x4b\xbb"
    n = t.write(strInput)  
    print n  
    str = t.read(50)  
    print str
    hexShow(str)
    str_line = "----------------------------------------------"
    print str_line

    strInput = "\xff\x03\x9b\x05\x00\x00\xdc\xe8"
    n = t.write(strInput)  
    print n  
    str = t.read(50)  
    print str
    hexShow(str)
    str_line = "----------------------------------------------"
    print str_line

    strInput = "\xff\x05\x91\x02\x01\x01\x04\x04\x2b\xc6"
    n = t.write(strInput)  
    print n  
    str = t.read(50)  
    print str
    hexShow(str)
    str_line = "----------------------------------------------"
    print str_line

    strInput = "\xff\x0b\x91\x03\x01\x0b\xb8\x0b\xb8\x04\x0a\x8c\x0a\x8c\xcb\xa7"
    n = t.write(strInput)  
    print n  
    str = t.read(50)  
    print str
    hexShow(str)
    str_line = "----------------------------------------------"
    print str_line

    strInput = "\xff\x00\x2a\x1d\x25"
    n = t.write(strInput)  
    print n  
    str = t.read(50)  
    print str
    hexShow(str)
    str_line = "----------------------------------------------"
    print str_line

    strInput = "\xFF\x05\x22\x00\x00\x03\x00\xC8\x38\x14"
    n = t.write(strInput)  
    print n  
    str = t.read(50)  
    print str
    hexShow(str)
    str_line = "----------------------------------------------"
    print str_line

    strInput = "\xFF\x03\x29\x00\x3F\x00\xCB\x22"
    n = t.write(strInput)  
    print n  
    str = t.read(200)  
    print str 
    hexid = hexShow(str).replace(" ","")
    epcid = hexid[50:74]
    print epcid
    return epcid

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
        personsn = get_personsn()
        info = {
            "personsn":personsn,
        }
        return info
 
if __name__ == "__main__":
    app.run()