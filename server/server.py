#coding:utf8
import socket
import Queue
import select
import traceback
import time
import requests

class ChatServer():
    api_url = "http://127.0.0.1:8000/monitor/report/"
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
        s.bind(('localhost',10001))
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
                msg = ts.recv(1024) #select检查到有数据时 除了连接就是接收数据
                if msg:#如果有数据
                    print 'read[%s]'%msg
                    protocol_header = msg[0:4]
                    protocol_stype = msg[4:6]
                    date_lenth = msg[6:8]
                    device_sn = msg[8:24]
                    # cmd,tmp = msg.split(None,1)#以一个空值分离一次 客户端cmd 的命令和数据
                    # print 'split[%s][%s]'%(cmd,tmp) 
                    if protocol_header != "464B":
                        print "protocol_header error"
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
                        if answer_status == "00":
                            msg = "success"
                        elif answer_status == "01":
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
                if not self.dict_msg[ts].empty():
                    msg = self.dict_msg[ts].get_nowait()#不等待，没有数据则直接引发异常
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

    def doAnswer(self,ts='',msg=''):
        if ts in self.device_web_map:
            web_socket = self.device_web_map[ts]
            self.dict_msg[web_socket].put(msg)
        else:
            print "web clinet close"

    def doWarning(self,ts='',device_sn='',msg=''):#对某人发
        # user,tmp = msg.split(None,1)
        user = device_sn
        tmp = msg
        find_user = 0
        for s in self.dict_name:
          if self.dict_name[s] == user: #当对某人发时取得某人的消息队列
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

        msg = "464B" + "02" + "xx" + sn + hex(year)[2:].upper() + hex(month)[2:].upper() + hex(day)[2:].upper() + \
        hex(week)[2:].upper() + hex(hour)[2:].upper() + hex(minute)[2:].upper() + hex(second)[2:].upper()
        lenth = len(msg)
        msg = msg.replace("xx",hex(lenth)[2:].upper())  
        self.dict_msg[ts].put(msg)
        return

    def process_data(self,ts='',device_sn='',data=''):
        sn = device_sn
        person_num = int(data[24:26],16)
        person_info = data[26:50]
        status = int(data[50:52],16)
        year = int(data[52:54],16) + 2000
        month = int(data[54:56],16)
        day = int(data[56:58],16)
        week = int(data[58:60],16)
        hour = int(data[60:62],16)
        minute = int(data[62:64],16)
        second = int(data[64:66])
        date = "%s-%s-%s %s:%s:%s" % (year,month,day,hour,minute,second)
        http_data = {
            "sn":sn,
            "person_num":person_num,
            "person_info":person_info,
            "status":status,
            "date":date,
        }
        re = requests.post(url=self.api_url, data=http_data)
        if re.status_code == 200:
            self.dict_msg[ts].put(re.text)
        else:
            self.dict_msg[ts].put(str(re.status_code))
        self.dict_msg[ts].put(str("ok"))

           
if __name__=='__main__':
    cs = ChatServer()
    cs.run()
