#  @时间：2022/1/6  20:05
#  @作者：简词海
#  @代码名字：studentRoot.py

import os
import sqlite3
import hashlib
import lib.UserName as un
import lib.logs as lo
import time


# import UserName as un

class Student(object):
    def __init__(self):
        self.userSql = ""
        self.sql = ""
        self.passwd = ""

    def sqlgai(self, id, user, conn, c):
        string1 = "姓名 性别 类别 住址 密码"
        dict1 = {"姓名": "NAME", "性别": "SEX", "类别": "student", "住址": "SITE", "密码": "PASSWD"}
        dict2 = {"年龄": "AGE", "电话": "PHONE", "身份证": "IDID"}
        if user in string1:
            user_in = input(f"请输入更改后的{user}：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把学号为：{id}的{user}更改成了：{user_in}")
            out = dict1.get(user)
            sql = """UPDATE JIAN set '%s' = '%s' where  ID = '%d'""" % (out, user_in, id)
        else:
            user_in = int(input(f"请输入更改后的{user}："))
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把学号为：{id}的{user}更改成了：{user_in}")
            out = dict2.get(user)
            sql = """UPDATE JIAN set '%s' = '%d' where  ID = '%d'""" % (out, user_in, id)
        c.execute(sql)
        conn.commit()

    def sqlgai1(self, id, user, conn, c):
        dict1 = {"语文": "LANGUAGE", "数学": "MATH", "外语": "FOREIGNS", "物理": "PHYSICS", "化学": "CHEMISTRY", "生物": "BIOLOGY",
                 "政治": "POLITICS", "历史": "HISTORY", "地理": "GEOG"}
        user_in = int(input(f"请输入更改后的{user}成绩:"))
        lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把学号为：{id}的{user}更改成了：{user_in}")
        out = dict1.get(user)
        sql = """UPDATE JIAN set '%s' = '%s' where  ID = '%d'""" % (out, user_in, id)
        c.execute(sql)
        conn.commit()
        sun = c.execute("select ID,LANGUAGE, MATH,FOREIGNS,PHYSICS,CHEMISTRY,BIOLOGY,POLITICS,HISTORY,GEOG from JIAN ")
        for i in sun:
            if int(id) == int(i[0]):
                total = int(i[1]) + int(i[2]) + int(i[3]) + int(i[4]) + \
                        int(i[5]) + int(i[6]) + int(i[7]) + int(i[8]) + int(i[9])
                sql = """UPDATE JIAN set TOTAL = '%d' where  ID = '%d'""" % (total, id)
                c.execute(sql)
                conn.commit()

    def studentSql(self, name):
        conn = sqlite3.connect(rf"C:\Xjian\student\{name}.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE JIAN
                                (ID INT PRIMARY KEY   NOT NULL,
                                NAME            TEXT  NOT NULL,
                                AGE             INT   NOT NULL,
                                SEX             TETX  NOT NULL,
                                CLASS           TEXT  NOT NULL,
                                PHONE           INT   NOT NULL,
                                IDID            INT   NOT NULL,
                                SITE            TEXT  NOT NULL,
                                LANGUAGE        INT   NOT NULL,
                                MATH            INT   NOT NULL,
                                FOREIGNS        INT   NOT NULL,
                                PHYSICS         INT   NOT NULL,
                                CHEMISTRY       INT   NOT NULL,
                                BIOLOGY         INT   NOT NULL,
                                POLITICS        INT   NOT NULL,
                                HISTORY         INT   NOT NULL,
                                GEOG            INT   NOT NULL,
                                TOTAL           INT   NOT NULL,
                                PASSWD          TEXT  NOT NULL);''')
        conn.commit()
        conn.close()
        lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 创建了一个名字为{name}的数据库")

    def addstudent(self, a):
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        while True:
            try:
                print("请输入学生的学号 姓名 年龄 性别 班级 电话 身份证 住址 语 数 外 物 化 生 政 史 地（用空格隔开，退出输入q）")
                studentUser = input("请输入以上信息：").split(" ")
                if studentUser[0] == "q":
                    conns.close()
                    print("正在返回主菜单")
                    return
                if len(studentUser) == 17:
                    total = int(studentUser[8]) + int(studentUser[9]) + int(studentUser[10]) + int(studentUser[11]) + \
                            int(studentUser[12]) + int(studentUser[13]) + int(studentUser[14]) + int(
                        studentUser[15]) + int(studentUser[16])
                    sql = '''INSERT INTO JIAN (ID, NAME, AGE, SEX, CLASS, PHONE,IDID,SITE,LANGUAGE,
                    MATH,FOREIGNS,PHYSICS,CHEMISTRY,BIOLOGY,POLITICS,HISTORY,GEOG,TOTAL,PASSWD)
                VALUES ('%d', '%s', '%d', '%s','%s', '%d', '%d', '%s', '%d', '%d','%d', '%d','%d', 
                '%d','%d', '%d', '%d','%d','%s')''' % (
                        int(studentUser[0]), studentUser[1], int(studentUser[2]), studentUser[3], studentUser[4],
                        int(studentUser[5]), int(studentUser[6]), studentUser[7], int(studentUser[8]),
                        int(studentUser[9]),
                        int(studentUser[10]), int(studentUser[11]), int(studentUser[12]), int(studentUser[13]),
                        int(studentUser[14]), int(studentUser[15]), int(studentUser[16]), total,
                        studentUser[6][12:]
                    )
                    c.execute(sql)
                    conns.commit()
                    lo.los(
                        f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 添加了一个学号为：{int(studentUser[0])}的学生")
                    print("添加成功\n")
                else:
                    print("参数不足")
            except Exception as f:
                print("去检查后输入")

    def delstudent(self, a):
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        while True:
            try:
                delstudent = input("请输入学生学号（退出输入q）：")
                if delstudent == "q":
                    conns.close()
                    return
                rootPasswd = input("为了安全起见，请输入root密码：")
                m = hashlib.md5()
                m.update(rootPasswd.encode(encoding="utf-8"))
                if self.passwd == m.hexdigest():
                    c.execute("DELETE from JIAN where ID ='%d';" % int(delstudent))
                    conns.commit()
                    print("删除成功")
                    lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 删除了一个学号为：{delstudent}的学生")
                else:
                    print("密码输入错误，删除失败")
            except Exception:
                print("请正确输入学号")

    def amendstudent(self, a):
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        while True:
            try:
                rootUser = input("请输入学号（退出输入q）：")
                if rootUser == "q":
                    conns.commit()
                    conns.close()
                    return
                sun = c.execute(
                    "select ID, NAME, AGE, SEX, CLASS, PHONE,IDID,SITE,LANGUAGE, MATH,FOREIGNS,PHYSICS,CHEMISTRY,BIOLOGY,POLITICS,HISTORY,GEOG,TOTAL,PASSWD from JIAN ")
                for i in sun:
                    if int(rootUser) == int(i[0]):
                        print(
                            f"学号：{i[0]} 姓名：{i[1]} 年龄：{i[2]} 性别：{i[3]} 班级：{i[4]} 电话：{i[5]} 身份证：{i[6]} 住址：{i[7]}\n 语文：{i[8]} 数学：{i[9]}"
                            f"外语：{i[10]} 物理：{i[11]} 化学：{i[12]}生物：{i[13]} 政治：{i[14]} 历史：{i[15]} 地理：{i[16]} 总分：{i[17]} 密码：{i[18]}")
                string = "姓名 年龄 性别 类别 电话 身份证 住址 密码"
                string1 = "语文 数学 外语 物理 化学 生物 政治 历史 地理"
                print(string, string1)
                user_id = input("请选择更改的项目：")
                if user_id in string:
                    self.sqlgai(int(rootUser), user_id, conns, c)
                    print("修改成功")
                elif user_id in string1:
                    self.sqlgai1(int(rootUser), user_id, conns, c)
                    print("更改成功")
            except Exception:
                print("输入错误，请检查后再输")

    def querystudent(self, a):
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        while True:
            userQuery = input("请输入学号（退出输入q）：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 查询了学号为：{userQuery}的学生")
            if userQuery == "q":
                conns.commit()
                c.close()
                return
            sun = c.execute(
                "select ID, NAME, AGE, SEX, CLASS, PHONE,IDID,SITE,LANGUAGE, MATH,FOREIGNS,PHYSICS,CHEMISTRY,BIOLOGY,POLITICS,HISTORY,GEOG,TOTAL,PASSWD from JIAN ")
            for i in sun:
                if int(userQuery) == int(i[0]):
                    print(
                        f"学号：{i[0]} 姓名：{i[1]} 年龄：{i[2]} 性别：{i[3]} 班级：{i[4]} 电话：{i[5]} 身份证：{i[6]} 住址：{i[7]}\n 语文：{i[8]} 数学：{i[9]}"
                        f"外语：{i[10]} 物理：{i[11]} 化学：{i[12]}生物：{i[13]} 政治：{i[14]} 历史：{i[15]} 地理：{i[16]} 总分：{i[17]} 密码：{i[18]}")

    def daochu(self, a):
        lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 导出了 {self.userSql}的数据库")
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        sun = c.execute("select ID, NAME, AGE, SEX, CLASS, PHONE,IDID,SITE,LANGUAGE, MATH,FOREIGNS,PHYSICS,CHEMISTRY,BIOLOGY,POLITICS,HISTORY,GEOG,TOTAL,PASSWD from JIAN ")
        f = open(fr"C:\Xjian\student\{self.userSql}.txt", "w")
        for i in sun:
            string = f"学号：{i[0]} 姓名：{i[1]} 年龄：{i[2]} 性别：{i[3]} 班级：{i[4]} 电话：{i[5]} 身份证：{i[6]} 住址：{i[7]}\n 语文：{i[8]} " \
                     f"数学：{i[9]}  外语：{i[10]} 物理：{i[11]} 化学：{i[12]}生物：{i[13]} 政治：{i[14]} 历史：{i[15]} 地理：{i[16]} 总分：{i[17]} " \
                     f"密码：{i[18]}"
            print(string)
            f.write(string + "\n")
        f.close()
        print("导出完成")

    def student(self):
        while True:
            f = open(r"C:\Xjian\Root\pwd.xjian", "r")
            passwd = f.readlines()
            self.passwd = passwd[0][:-1]
            f.close()
            print("""
            1，创建/删除 学生数据库
            2，添加学生信息
            3，删除学生信息
            4，修改学生信息
            5，查找学生信息
            6，导出所有学生信息
            7,退出
    """)
            dict1 = {"1": self.studentSql, "2": self.addstudent, "3": self.delstudent, "4": self.amendstudent,
                     "5": self.querystudent, "6": self.daochu}
            dict2 = {"1": "创建/删除 学生数据库",
                     "2": "添加学生信息",
                     "3": "删除学生信息",
                     "4": "修改学生信息",
                     "5": "查找学生信息",
                     "6": "导出所有学生信息",
                     "7": "退出"}

            userRoot = input("请输入序号：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} {dict2.get(userRoot)}")
            if userRoot == "7":
                return
            if not os.listdir(r"C:\Xjian\student") or userRoot == "1":
                sqlName = input("请输入数据库名字：")
                self.studentSql(sqlName)
                continue
            name = dict1.get(userRoot, "-1")
            if name == "-1":
                continue
            print([i[:-3] for i in os.listdir(r"C:\Xjian\student")], "\n请选择数据库")
            userSql = input("请输入：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 选择数据库为：{userSql}")
            self.sql = rf"C:\Xjian\student\{userSql}.db"
            self.userSql = userSql
            name(3)
#
# App = Student()
# App.student()