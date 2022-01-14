#  @时间：2022/1/1  22:39
#  @作者：简词海
#  @代码名字：Mails.py

import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail(object):
    def __init__(self, Hos):
        self.mail_host = "smtp.qq.com"
        self.mail_user = "2835673066@qq.com"
        self.mail_pass = ""   # 设置授权码
        self.user = "2835673066@qq.com"
        self.string = "欢迎使用学生管理系统，您的验证码为："
        self.age = str(random.randint(100000, 999999))
        self.hos = Hos

    def mails(self):
        txt = MIMEText(self.string + self.age, 'plain', "utf-8")
        txt["From"] = Header("小简科技", 'utf-8')
        txt['To'] = Header("您", 'utf-8')
        txt['Subject'] = Header("欢迎光临", 'utf-8')
        try:
            stmp = smtplib.SMTP()
            stmp.connect(self.mail_host, 25)
            stmp.login(self.user, self.mail_pass)
            stmp.sendmail(self.user, self.hos, txt.as_string())
        except smtplib.SMTPException:
            pass
        return self.age
