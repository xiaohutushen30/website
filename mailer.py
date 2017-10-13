# coding=utf-8
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import smtplib
import socket


class EmailUtils(object):
    def __init__(self):
        super(EmailUtils, self).__init__()
        self.mail_host = ''
        self.mail_from = ''
        self.mail_pass = ''
        self.server = None
        self.login()

    def login(self):
        self.server = smtplib.SMTP()
        self.server.connect(self.mail_host, "25")
        # self.server.starttls()
        self.server.login(self.mail_from, self.mail_pass)

    def add_attch(self, to_list, subject, content, path):
        content_type = 'html' if content.startswith('<html>') else 'plain'
        msg = MIMEMultipart('related')
        msgtext = MIMEText(content, _subtype=content_type, _charset='utf-8')
        msg.attach(msgtext)
        if path:
            attach = MIMEText(open(path, 'rb').read())
            attach["Content-Type"] = 'application/octet-stream'
            attach["Content-Disposition"] = 'attachment; filename=' + path.encode("gb2312")
            msg.attach(attach)
        msg['Subject'] = subject
        msg['From'] = self.mail_from
        msg['To'] = COMMASPACE.join(to_list)
        msg['Date'] = formatdate(localtime=True)
        return msg

    def send_mail(self, msg):
        mtries, mdelay = 3, 0.5
        while mtries > 1:
            try:
                if not self.server:
                    self.login()
                self.server.sendmail(self.mail_from, msg['To'], msg.as_string())
                status, reason= True, "ok"
                return status, reason

            except socket.gaierror as ex:
                """ 网络无法连接 """
                self.server = None
                rs = "%s, Retrying in %d seconds..." % (str(ex), mdelay)
                time.sleep(mdelay)
                mtries -= 1
                status, reason = False, rs

            except smtplib.SMTPServerDisconnected as ex:
                """ 网络连接异常 """
                self.server = None
                rs = "%s, Retrying in %d seconds..." % (str(ex), mdelay)
                time.sleep(mdelay)
                mtries -= 1
                status, reason = False, rs

            except smtplib.SMTPException as ex:
                """ 邮件发送异常 """
                rs = "%s, Retrying in %d seconds..." % (str(ex), mdelay)
                time.sleep(mdelay)
                mtries -= 1
                status, reason = False, rs

            except Exception as ex:
                """未知异常"""
                rs = "%s, Retrying in %d seconds..." % (str(ex), mdelay)
                time.sleep(mdelay)
                mtries -= 1
                status, reason = False, rs
        return status, reason

    def __del__(self):
        self.server.quit()


if __name__ == '__main__':
    mail = EmailUtils()
    msg = mail.add_attch([''], u'主题测试', u'关于邮件发送的测试', u'邮件附件.txt')
    mail.send_mail(msg)
