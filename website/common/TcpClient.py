#coding:utf8
import cmd, socket, traceback, threading, time
import sys
class ChatClient(cmd.Cmd):
    ''' chat client '''
    def __init__(self, host='127.0.0.1', port=49999):
        cmd.Cmd.__init__(self)
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.sock = ''
        self.name = ''
        
    def do_connect(self,timeout = 1):#连接到server
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((self.host, self.port))
        s.settimeout(timeout)#设置超时时间 0.1 秒
        self.sock = s
       
    def do_EOF(self):#退出
        if self.sock:
            self.sock.close()
        return True
    
    
if __name__=='__main__':
    # ChatClient().cmdloop()
    chat_client = ChatClient()
    chat_client.do_connect()
    # chat_client.do_name("jsdfjasdhfjshfshakjhfasljhaslf")
    chat_client.sock.send("464B04211FFFF7F01FFFF7E8")
    msg = None
    while not msg:
        try:
            msg = chat_client.sock.recv(1024) #新建对象
            print msg
        except socket.timeout:
            pass
    chat_client.sock.close()