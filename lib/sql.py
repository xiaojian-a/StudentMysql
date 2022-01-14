#  @时间：2022/1/7  20:06
#  @作者：简词海
#  @代码名字：sql.py
import hashlib
import os


def sqls():
    f = open(r"C:\Xjian\Root\pwd.xjian", "r")
    passwd = f.readlines()
    passwd = passwd[0][:-1]
    f.close()
    user = input("请选择删除的对象：1，老师  2，学生  ：")
    if user == "老师":
        print([i[:-3] for i in os.listdir(r"C:\Xjian\teacher")])
        rootPasswd = input("为了安全起见，请输入root密码：")
        m = hashlib.md5()
        m.update(rootPasswd.encode(encoding="utf-8"))
        if passwd == m.hexdigest():
            user_sql = input("请选择数据库名称：")
            os.remove(rf"C:\Xjian\teacher\{user_sql}.db")
            print("删除成功")
            return
        else:
            print("密码输入错误")
    elif user == "学生":
        print([i[:-3] for i in os.listdir(r"C:\Xjian\student")])
        rootPasswd = input("为了安全起见，请输入root密码：")
        m = hashlib.md5()
        m.update(rootPasswd.encode(encoding="utf-8"))
        if passwd == m.hexdigest():
            user_sql = input("请选择数据库名称：")
            os.remove(rf"C:\Xjian\student\{user_sql}.db")
            print("删除成功")
            return
        else:
            print("密码输入错误")

    else:
        print("输入错误")
