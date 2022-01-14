#  @时间：2022/1/6  21:23
#  @作者：简词海
#  @代码名字：Teacher.py
import os
import sqlite3
import time
import lib.logs as lo


class Teacher(object):
    def __init__(self, teacher, con, c, tea):
        self.sql = ""
        self.userSql = ""
        self.id = int(teacher[0])
        self.passwd = teacher[1]
        self.coons = con
        self.c = c
        self.teacher = tea

    def personal(self):
        while True:
            try:
                sun = self.c.execute("select ID, NAME, AGE, SEX, PHONE,IDID,SITE,IC from JIAN ")
                for i in sun:
                    if self.id == int(i[0]):
                        print(f"""
                        工号：{i[0]} 姓名：{i[1]} 年龄：{i[2]} 性别：{i[3]} 
                        电话：{i[4]} 身份证：{i[5]} 住址：{i[6]} 银行卡：{i[7]}"
                        """)
                string = "姓名 年龄 性别 电话 身份证 住址 银行卡 密码"
                print("\n请选择修改的项目：" + string)
                user_id = input("请选择更改的项目(退出输入q)：")
                if user_id in string:
                    self.sqlgai(self.id, user_id, self.coons, self.c)
                    print("修改成功")
                if user_id == "q":
                    self.coons.commit()
                    self.coons.close()
                    return
            except Exception:
                print("输入错误，请检查后再输")

    def sqlgai1(self):
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        dict1 = {"语文": "LANGUAGE", "数学": "MATH", "外语": "FOREIGNS", "物理": "PHYSICS", "化学": "CHEMISTRY", "生物": "BIOLOGY",
                 "政治": "POLITICS", "历史": "HISTORY", "地理": "GEOG"}
        user_id = int(input("请输入学生学号(退出输入q)："))
        if user_id == "q":
            conns.commit()
            return
        user = dict1.get(self.teacher)

        sun = c.execute("select ID,NAME, LANGUAGE, MATH,FOREIGNS,PHYSICS,CHEMISTRY,BIOLOGY,POLITICS,HISTORY,GEOG, TOTAL from JIAN ")
        for i in sun:
            if user_id == int(i[0]):
                print(f"学号：{i[0]} 姓名：{i[1]}\n语文：{i[2]} 数学：{i[3]}"
                      f"外语：{i[4]} 物理：{i[5]} 化学：{i[6]}生物：{i[7]} 政治：{i[8]} 历史：{i[9]} 地理：{i[10]} 总分：{i[11]}")
        user_in = int(input(f"请输入更改后的{self.teacher}成绩:"))
        sql = """UPDATE JIAN set '%s' = '%s' where  ID = '%d'""" % (user, user_in, user_id)
        lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把学号为：{user_id}的{user}更改成了：{user_in}")
        c.execute(sql)
        conns.commit()
        sun = c.execute("select ID,LANGUAGE, MATH,FOREIGNS,PHYSICS,CHEMISTRY,BIOLOGY,POLITICS,HISTORY,GEOG from JIAN ")
        for i in sun:
            if user_id == int(i[0]):
                total = int(i[1]) + int(i[2]) + int(i[3]) + int(i[4]) + \
                        int(i[5]) + int(i[6]) + int(i[7]) + int(i[8]) + int(i[9])
                sql = """UPDATE JIAN set TOTAL = '%d' where  ID = '%d'""" % (total, user_id)
        c.execute(sql)
        conns.commit()
        conns.close()

    def admStudent(self):
        print([i[:-3] for i in os.listdir(r"C:\Xjian\student")], "\n请选择数据库")
        userSql = input("请输入：")
        lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 老师选择数据库为：{userSql}进行操作")
        self.sql = rf"C:\Xjian\student\{userSql}.db"
        self.userSql = userSql
        self.sqlgai1()

    def sqlgai(self, id, user, conns, c):
        string1 = "姓名 性别 住址 密码"
        dict1 = {"姓名": "NAME", "性别": "SEX", "住址": "SITE", "密码": "PASSWD"}
        dict2 = {"年龄": "AGE", "电话": "PHONE", "身份证": "IDID", "银行卡": "IC"}
        if user in string1:
            user_in = input(f"请输入更改后的{user}：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把工号为：{id}的{user}更改成了：{user_in}")
            out = dict1.get(user)
            if out == "PASSWD":
                print("请输入原始密码：")
                user = input("请输入：")
                if not user == self.passwd:
                    print("密码输入错误，请检查后输入")
                    return
            sql = """UPDATE JIAN set '%s' = '%s' where  ID = '%d'""" % (out, user_in, id)
        else:
            user_in = int(input(f"请输入更改后的{user}："))
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把工号为：{id}的{user}更改成了：{user_in}")
            out = dict2.get(user)
            sql = """UPDATE JIAN set '%s' = '%d' where  ID = '%d'""" % (out, user_in, id)
        c.execute(sql)
        conns.commit()
