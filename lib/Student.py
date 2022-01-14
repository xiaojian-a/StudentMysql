#  @时间：2022/1/6  22:25
#  @作者：简词海
#  @代码名字：Student.py


import os
import sqlite3
import time
import lib.logs as lo


class Student(object):
    def __init__(self, student, con, c, pwd):
        self.sql = ""
        self.userSql = ""
        self.id = int(student[0])
        self.passwd = student[1]
        self.coons = con
        self.c = c
        self.student = pwd

    def personal(self,user_id):
        string1 = "性别 住址 密码"
        dict1 = {"住址": "SITE", "密码": "PASSWD"}
        dict2 = {"年龄": "AGE", "电话": "PHONE", "身份证": "IDID"}
        if user_id in string1:
            user_in = input(f"请输入更改后的{user_id}：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把学号为：{self.id}的{user_id}更改成了：{user_in}")
            out = dict1.get(user_id)
            sql = """UPDATE JIAN set '%s' = '%s' where  ID = '%d'""" % (out, user_in, self.id)
        else:
            user_in = int(input(f"请输入更改后的{user_id}："))
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把学号为：{self.id}的{user_id}更改成了：{user_in}")
            out = dict2.get(user_id)
            sql = """UPDATE JIAN set '%s' = '%d' where  ID = '%d'""" % (out, user_in, self.id)
        self.c.execute(sql)
        self.coons.commit()

    def amendstudent(self):
        while True:
            try:
                sun = self.c.execute(
                    "select ID, NAME, AGE, SEX, PHONE,IDID,SITE,PASSWD from JIAN ")
                for i in sun:
                    if self.id == int(i[0]):
                        print(f"学号：{i[0]} 姓名：{i[1]} 年龄：{i[2]} 性别：{i[3]} 电话：{i[4]} 身份证：{i[5]} 住址：{i[6]} 密码：{i[7]}")
                string = " 年龄 电话 身份证 住址 密码"
                print(string)
                user_id = input("请选择更改的项目(退出输入q)：")
                if user_id == "q":
                    self.coons.commit()
                    self.coons.close()
                    return
                if user_id in string:
                    self.personal(user_id)
                    print("修改成功")
            except Exception:
                print("输入错误，请检查后再输")

    def queryStudent(self):
        while True:
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 查询了学号为：{self.id}的学生")

            sun = self.c.execute(
                "select ID, NAME,LANGUAGE, MATH,FOREIGNS,PHYSICS,CHEMISTRY,BIOLOGY,POLITICS,HISTORY,GEOG,TOTAL from JIAN ")
            for i in sun:
                if self.id == int(i[0]):
                    print(
                        f"学号：{i[0]} 姓名：{i[1]} 语文：{i[2]} 数学：{i[3]}"
                        f"  外语：{i[4]} 物理：{i[5]} 化学：{i[6]}生物：{i[7]} 政治：{i[8]} 历史：{i[9]} 地理：{i[10]} 总分：{i[11]}")
                    return



