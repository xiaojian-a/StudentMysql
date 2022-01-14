#  @时间：2022/1/1  22:02
#  @作者：简词海
#  @代码名字：OsMkdir.py
import os
import hashlib
import lib.passwds as ps

def mkdir():
    print("""
        =============================================
                      欢迎使用小简科技学生管理系统
        =============================================
    """)
    os.mkdir(r"C:\Xjian")
    os.mkdir(r"C:\Xjian\logs")
    os.mkdir(r"C:\Xjian\teacher")
    os.mkdir(r"C:\Xjian\student")
    os.mkdir(r"C:\Xjian\Root")
    f1 = open(r"C:\Xjian\logs\los.lg", "w")
    f1.close()
    f = open(r"C:\Xjian\Root\pwd.xjian", "w")
    while True:
        user_pwd = input("请先设置密码：")
        if ps.lens(user_pwd):
            m1 = hashlib.md5()
            m1.update(user_pwd.encode(encoding="utf-8"))
            break
        else:
            print("密码强度不够")
    while True:
        user_mail = input("请设置邮箱：")
        if ps.mila(user_mail):
            m2 = hashlib.md5()
            m2.update(user_mail.encode(encoding="utf-8"))
            break
        else:
            print("邮箱不符合规则")
    user_w = input("请设置安全问题：")
    user_d = input("请设置答案：")
    m3 = hashlib.md5()
    m3.update(user_d.encode(encoding="utf-8"))
    f.write(f"{m1.hexdigest()}\n{m2.hexdigest()}\n{user_w}={m3.hexdigest()}")
    f.close()

