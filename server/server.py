#coding:utf8
import socket
import Queue
import select
import traceback
import time
import requests
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import threading
import binascii
import json

clients = []
class TCPServer():
    api_url = "http://127.0.0.1:8000/monitor/report/"
    addroomurl = "http://127.0.0.1:8000/room/room/addroomapi/"
    def __init__(self):
        self.dict_name = {}#客户端和设备对应
        self.dict_msg = {}#客户端和消息队列对应
        self.listen_fd = 0#初始化监听的文件描述符
        self.inputs = []#可读状态列表
        self.outputs = []#可写状态列表
        self.device_web_map = {}#客户端和web客户端对应列表

    def run(self):
        ''' 用select监听socket'''
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#默认ip tcp、协议
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#地址复用
        local_ip = socket.gethostbyname(socket.gethostname())
        s.bind((local_ip,49999))
        print "local ip:",local_ip
        s.listen(1)
        self.inputs.append(s)#将s加入到监听的列表 
        self.listen_fd = s#将要监听的文件描述符覆给listen_fd
        while True:
            list_r,list_w,list_e = select.select(self.inputs,self.outputs,self.inputs)
            '''
                监听刚刚创建的文件描述符（inputs列表中），如果有连接到socket就select将s写到lis_r中
                如果有数据发送加入lis_w中进行操作，如果有异常在lis_e中操作
                确定第一次select检测到的状态肯定是新客户端连接进来了
            '''
            if self.listen_fd in list_r:#如果s在可写状态可能是有连接或者有数据
                conn,cli = self.listen_fd.accept()#新建一个文件描述符 来进行客户端与服务器的通信
                self.dict_name[conn] = '' #新的文件描述符加入到字典
                self.dict_msg[conn] = Queue.Queue()#将客户端加入到对应的消息队列
                self.inputs.append(conn) #将新的文件描述符加入到监听列表中
                print 'new connects',conn.getpeername() #getpeername()：获取已连接成功之 Socket 的对方位址。 
            '''
                连接成功后开始处理 select流
            '''
            self.doExcept(list_e)
            self.doRead(list_r)
            self.doWrite(list_w)
            time.sleep(0.1)
    def doRead(self,list_r=[]):
        for ts in list_r:
            if ts is self.listen_fd:continue#如果是监听的socket 就继续
            try:
                try:
                    msg = ts.recv(1024) #select检查到有数据时 除了连接就是接收数据
                except:
                    self.doExcept([ts])
                    msg = None
                if msg:#如果有数据
                    print "rec %s"%msg
                    msg = binascii.b2a_hex(msg).upper()
                    print 'read[%s]' % msg
                    protocol_header = msg[0:4]
                    protocol_stype = msg[4:6]
                    data_lenth = msg[6:8]
                    device_sn = msg[8:24]
                    if protocol_header != "464B":
                        print "protocol_header error"
                        continue
                    real_length = len(msg)/2
                    if real_length != int(data_lenth,16):
                        print "protocol length is error"
                        continue
                    if protocol_stype == '00':#链接
                        self.doName(ts,device_sn)
                    elif protocol_stype == '01':#时间同步
                        self.process_time(ts,device_sn)
                    elif protocol_stype == '03':#上报人员信息
                        self.process_data(ts,device_sn,msg)
                    elif protocol_stype == "04":
                        self.doWarning(ts,device_sn,msg)
                    elif protocol_stype == "05":
                        answer_status = msg[24:26]
                        if answer_status == "01":
                            msg = "success"
                        elif answer_status == "00":
                            msg = "failure"
                        else:
                            msg = "unknown"
                        self.doAnswer(ts,msg)
                    else:
                        self.doMsg(ts,tmp)
                    if ts not in self.outputs:#准备发送给客户端
                        self.outputs.append(ts)
                else:
                    self.doExcept([ts])
                print 'read',ts.fileno(),len(msg) #打开文件描述符
            except:
                traceback.print_exc()
    def doWrite(self,list_w=[]):
        for ts in list_w:
            try:
                if not self.dict_msg.get(ts):
                    list_w.remove(ts)
                    continue
                if not self.dict_msg.get(ts).empty():
                    msg = self.dict_msg[ts].get_nowait()#不等待，没有数据则直接引发异常
                    #msg = binascii.a2b_hex(msg)
                    if msg:
                        ts.send(msg)
                    print 'write',ts.fileno(),len(msg)
            except:
                traceback.print_exc()
    def doExcept(self,list_e=[]):#异常的处理
        for ts in list_e:
            if ts in self.inputs:#如果异常则不再监听将各个队列的文件描述符删除
                self.inputs.remove(ts)
            if ts in self.outputs:
                self.outputs.remove(ts)
            if ts in self.dict_name:
                del self.dict_name[ts]
            if ts in self.dict_msg:
                del self.dict_msg[ts]
            if ts in self.device_web_map:
                del self.device_web_map[ts]
            print 'except',ts.fileno()
        
    def doName(self,ts='',tmp=''):#ts接收发过的数据 tmp 登陆聊天室
        self.dict_name[ts] = tmp#客户端对应发送的消息聊天人的姓名
        http_data = {
            "roomsn":tmp,
            "name":tmp,
        }
        re = requests.post(url=self.addroomurl, data=http_data)
        if re.status_code == 200:
            print "room option ok"
        else:
            print "room option failed %s" % str(re.status_code)

    def doAnswer(self,ts='',msg=''):
        if ts in self.device_web_map:
            web_socket = self.device_web_map[ts]
            web_socket.send(msg)
        else:
            print "web clinet close"

    def doWarning(self,ts='',device_sn='',msg=''):#对某人发
        # user,tmp = msg.split(None,1)
        #import pdb;pdb.set_trace()
        #print "device_sn:"%str(device_sn)
        user = device_sn
        tmp = msg
        find_user = 0
        for s in self.dict_name:
          if self.dict_name[s] == user: #当对某人发时取得某人的消息队列
            tmp = binascii.a2b_hex(tmp)
            print "send:%s"%tmp
            self.dict_msg[s].put(tmp)#发送用户名 消息 
            self.device_web_map[s] = ts
            find_user = 1
            break
        if not find_user:
            self.dict_msg[ts].put('user [%s] not found, and private msg not sent successfully' % find_user)

    def process_time(self,ts='',device_sn=''):
        sn = device_sn
        date_str = time.strftime("%Y %m %d %H %M %S %w",time.localtime())
        date_list = date_str.split(" ")
        year = int(date_list[0]) - 2000
        month = int(date_list[1])
        day = int(date_list[2])
        hour = int(date_list[3])
        minute = int(date_list[4])
        second = int(date_list[5])
        week = int(date_list[6])
        print year,month,day,hour,minute,second,week
        msg = "464B" + "02" + "xx" + sn + self.process_hex(year) + self.process_hex(month) + self.process_hex(day) + \
        self.process_hex(week) + self.process_hex(hour) + self.process_hex(minute) + self.process_hex(second)
        lenth = len(msg)
        msg = msg.replace("xx",self.process_hex(lenth/2))  
        msg = binascii.a2b_hex(msg)
        self.dict_msg[ts].put(msg)
        return

    def process_hex(self, num):
        hex_num = hex(num)[2:].upper()
        if len(hex_num) == 1:
            hex_num = "0"+hex_num
        return hex_num

    def process_data(self,ts='',device_sn='',data=''):
        sn = device_sn
        ir_person_num = int(data[24:26],16)
        frid_person_num = int(data[26:28],16)
        #非人员信息长度21
        persons_len = len(data) - 22*2
        #一条人员信息长度13
        if persons_len % (13*2) != 0:
            print "persons info is error!"
            return
        #ir_person_num = int(data[-2:],16)
        index = 28
        person_info = []
        for pnum in xrange(1,frid_person_num+1):
            person = {}
            tmp_person_infos = data[index:index+26]
            person["info"] = tmp_person_infos[0:24]
            person["status"] = int(tmp_person_infos[24:],16)
            person_info.append(person)
            index = index + 26
        # person_info = ",".join(person_info)
        # status = int(data[index:index+2],16)
        # index += 2
        year = int(data[index:index+2],16) + 2000
        index += 2
        month = int(data[index:index+2],16)
        index += 2
        day = int(data[index:index+2],16)
        index += 2
        week = int(data[index:index+2],16)
        index += 2
        hour = int(data[index:index+2],16)
        index += 2
        minute = int(data[index:index+2],16)
        index += 2
        second = int(data[index:index+2],16)
        date = "%s-%s-%s %s:%s:%s" % (year,month,day,hour,minute,second)
        print date
        # import pdb;pdb.set_trace()
        http_data = {
            "sn":sn,
            "person_num":ir_person_num,
            "persons_real_num":frid_person_num,
            "person_info":json.dumps(person_info),
            "date":date,
        }
        re = requests.post(url=self.api_url, data=http_data)
        if re.status_code == 200:
            print "report ok"
        else:
            print "report failed %s" % str(re.status_code)
        if clients:
            for client in clients:
                client.sendMessage(unicode("notice"))
        #self.dict_msg[ts].put(str("ok"))
        #print "report ok"

class WebSocketServer(WebSocket):

    def handleMessage(self):
        for client in clients:
            if client != self:
                client.sendMessage(self.address[0] + u' - ' + self.data)

    def handleConnected(self):
        print self.address, 'connected'
        for client in clients:
            client.sendMessage(self.address[0] + u' - connected')
        clients.append(self)

    def handleClose(self):
        clients.remove(self)
        print self.address, 'closed'
        for client in clients:
            client.sendMessage(self.address[0] + u' - disconnected')


if __name__=='__main__':
    server1 = SimpleWebSocketServer('', 8088, WebSocketServer)
    web_server = threading.Thread(target=server1.serveforever)
    server2 = TCPServer()
    tcp_server = threading.Thread(target=server2.run)
    threads = [web_server,tcp_server]
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    
