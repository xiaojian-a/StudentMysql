#  @时间：2022/1/4  20:24
#  @作者：简词海
#  @代码名字：user.py
import hashlib
import os
import sqlite3
import time
import lib.logs as lo
from lib import teacherRoot as te, sql
import lib.studentRoot as st
import lib.Teacher as teacher
import lib.Student as stu

def rootUser():
    f = open(r"C:\Xjian\Root\pwd.xjian", "r")
    userName = f.readlines()
    print("请输入账号 密码，用空格隔开")
    userRoot = input("请输入").split(" ")
    if len(userRoot) == 2:
        m = hashlib.md5()
        m.update(userRoot[1].encode(encoding="utf-8"))
        if userRoot[0] == "root" and m.hexdigest() == userName[0][:-1]:
            while True:
                lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} root登录成功")
                print("""
                            欢迎超级管理员回来~~
                     1，老师操作    2，学生操作  3，查看日志  4，删除数据库  5,退出
                """)
                root = input("请输入：")
                if root == "1":
                    lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} root选择老师操作")
                    te.Teacher().teacher()
                elif root == "2":
                    lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} root选择学生操作")
                    st.Student().student()

                elif root == "3":
                    f = open(r"C:\Xjian\logs\los.lg", "r")
                    name = f.readlines()
                    for i in name:
                        print(i)
                    f.close()

                elif root == "4":
                    sql.sqls()

                elif root == "5":
                    return
                else:
                    print("输入错误")
        else:
            print("登录失败，密码错误")
    else:
        print("参数不足")


def teacherUser():
    conns = sqlite3.connect(r"C:\Xjian\teacher\老师.db")
    c = conns.cursor()
    while True:
        print("请输入账号 密码，用空格隔开")
        userTeacher = input("请输入").split(" ")
        sun = c.execute("select ID, TEACHER, PASSWD from JIAN ")
        for i in sun:
            if int(userTeacher[0]) == int(i[0]) and userTeacher[1] == i[2]:
                while True:
                    lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 老师登录成功")
                    print("""
                                欢迎老师回来回来~~
                         1，个人中心    2，学生成绩导入  3,退出
                    """)
                    user_in = input("请输入：")
                    if user_in == "1":
                        teacher.Teacher(userTeacher, conns,c, i[1]).personal()
                    elif user_in == "2":
                        teacher.Teacher(userTeacher, conns,c, i[1]).admStudent()
                    elif user_in == "3":
                        conns.close()
                        return
                    else:
                        print("输入错误")


def studentUser():
    ls = [i[:-3] for i in os.listdir(r"C:\Xjian\student")]
    print(ls, "\n请选择班级")
    user_class = input("请输入：")
    if user_class in ls:
        conns = sqlite3.connect(fr"C:\Xjian\student\{user_class}.db")
        c = conns.cursor()
        while True:
            print("请输入账号 密码，用空格隔开")
            userStudent = input("请输入").split(" ")
            sun = c.execute("select ID, PASSWD from JIAN ")
            for i in sun:
                if int(userStudent[0]) == int(i[0]) and userStudent[1] == i[1]:
                    while True:
                        lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 学生登录成功")
                        print("""
                                    欢迎学生回来回来~~
                             1，个人中心    2，学生成绩查询  3,退出
                        """)
                        user_in = input("请输入：")
                        if user_in == "1":
                            stu.Student(userStudent, conns,c, i[1]).amendstudent()
                        elif user_in == "2":
                            stu.Student(userStudent, conns,c, i[1]).queryStudent()
                        elif user_in == "3":
                            conns.close()
                            return
                        else:
                            print("输入错误")
    else:
        print("输入有误")