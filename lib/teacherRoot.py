#  @时间：2022/1/4  21:06
#  @作者：简词海
#  @代码名字：teacherRoot.py
import os
import sqlite3
import hashlib
import lib.UserName as un
import lib.logs as lo
import time


# import UserName as un

class Teacher(object):
    def __init__(self):
        self.userSql = ""
        self.sql = ""
        self.passwd = ""

    def sqlgai(self, id, user, conn, c):
        string1 = "姓名 性别 类别 住址 密码"
        dict1 = {"姓名": "NAME", "性别": "SEX", "类别": "TEACHER", "住址": "SITE", "密码": "PASSWD"}
        dict2 = {"年龄": "AGE", "电话": "PHONE", "身份证": "IDID", "工资": "WAGE", "银行卡": "IC"}
        if user in string1:
            user_in = input(f"请输入更改后的{user}：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把工号为：{id}的{user}更改成了：{user_in}")
            out = dict1.get(user)
            sql = """UPDATE JIAN set '%s' = '%s' where  ID = '%d'""" % (out, user_in, id)
        else:
            user_in = int(input(f"请输入更改后的{user}："))
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 把工号为：{id}的{user}更改成了：{user_in}")
            out = dict2.get(user)
            sql = """UPDATE JIAN set '%s' = '%d' where  ID = '%d'""" % (out, user_in, id)
        c.execute(sql)
        conn.commit()

    def teacherSql(self, name):
        conn = sqlite3.connect(rf"C:\Xjian\teacher\{name}.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE JIAN
                                (ID INT PRIMARY KEY   NOT NULL,
                                NAME            TEXT  NOT NULL,
                                AGE             INT   NOT NULL,
                                SEX             TETX  NOT NULL,
                                TEACHER         TEXT  NOT NULL,
                                PHONE           INT   NOT NULL,
                                IDID            INT   NOT NULL,
                                SITE            TEXT  NOT NULL,
                                WAGE            INT   NOT NULL,
                                IC              INT   NOT NULL,
                                PASSWD          TEXT  NOT NULL);''')
        conn.commit()
        conn.close()
        lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 创建了一个名字为{name}的数据库")

    def addTeacher(self, a):
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        while True:
            try:
                print("请输入老师的工号 姓名 年龄 性别 类别 电话 身份证 住址 工资 银行卡（用空格隔开，退出输入q）")
                teacherUser = input("请输入以上信息：").split(" ")
                if teacherUser[0] == "q":
                    conns.close()
                    print("正在返回主菜单")
                    return
                if len(teacherUser) == 10:
                    if not teacherUser[1][0] in un.name():
                        continue
                    if 5 >= int(teacherUser[2]) >= 100:
                        continue
                    if not (teacherUser[3] == "男" or teacherUser[3] == "女"):
                        continue
                    sql = '''INSERT INTO JIAN (ID, NAME, AGE, SEX, TEACHER, PHONE,IDID,SITE,WAGE,IC,PASSWD)
                VALUES ('%d', '%s', '%d', '%s','%s', '%d', '%d', '%s', '%d', '%d', '%s')''' % (
                        int(teacherUser[0]), teacherUser[1], int(teacherUser[2]), teacherUser[3], teacherUser[4],
                        int(teacherUser[5]),
                        int(teacherUser[6]), teacherUser[7], int(teacherUser[8]), int(teacherUser[9]),
                        teacherUser[6][12:]
                    )
                    c.execute(sql)
                    conns.commit()
                    lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 添加了一个工号为：{int(teacherUser[0])}的老师")
                    print("添加成功\n")
                else:
                    print("参数不足")
            except Exception as f:
                print("去检查后输入")

    def delTeacher(self, a):
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        while True:
            try:
                delTeacher = input("请输入老师工号（退出输入q）：")
                if delTeacher == "q":
                    conns.close()
                    return
                rootPasswd = input("为了安全起见，请输入root密码：")
                m = hashlib.md5()
                m.update(rootPasswd.encode(encoding="utf-8"))
                if self.passwd == m.hexdigest():
                    c.execute("DELETE from JIAN where ID='%d';" % int(delTeacher))
                    conns.commit()
                    print("删除成功")
                    lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 删除了一个工号为：{delTeacher}的老师")
                else:
                    print("密码输入错误，删除失败")
            except Exception:
                print("请正确输入工号")

    def amendTeacher(self, a):
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        while True:
            try:
                rootUser = input("请输入工号（退出输入q）：")
                if rootUser == "q":
                    conns.commit()
                    conns.close()
                    return
                sun = c.execute("select ID, NAME, AGE, SEX, TEACHER, PHONE,IDID,SITE,WAGE,IC,PASSWD from JIAN ")
                for i in sun:
                    if int(rootUser) == int(i[0]):
                        print(
                            f"工号：{i[0]} 姓名：{i[1]} 年龄：{i[2]} 性别：{i[3]} 类别：{i[4]} 电话：{i[5]} 身份证：{i[6]} 住址：{i[7]} 工资：{i[8]} 银行卡：{i[9]} 密码：{i[10]}")
                string = "姓名 年龄 性别 类别 电话 身份证 住址 工资 银行卡 密码"
                print(string)
                user_id = input("请选择更改的项目：")
                if user_id in string:
                    self.sqlgai(int(rootUser), user_id, conns, c)
                    print("修改成功")
            except Exception:
                print("输入错误，请检查后再输")

    def queryTeacher(self, a):
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        while True:
            userQuery = input("请输入工号（退出输入q）：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 查询了工号为：{userQuery}的老师")
            if userQuery == "q":
                conns.commit()
                c.close()
                return
            sun = c.execute("select ID, NAME, AGE, SEX, TEACHER, PHONE,IDID,SITE,WAGE,IC,PASSWD from JIAN ")
            for i in sun:
                if int(userQuery) == int(i[0]):
                    print(
                        f"工号：{i[0]} 姓名：{i[1]} 年龄：{i[2]} 性别：{i[3]} 类别：{i[4]} 电话：{i[5]} 身份证：{i[6]} 住址：{i[7]} 工资：{i[8]} 银行卡：{i[9]} 密码：{i[10]}")

    def daochu(self, a):
        lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 导出了 {self.userSql}的数据库")
        conns = sqlite3.connect(self.sql)
        c = conns.cursor()
        sun = c.execute("select ID, NAME, AGE, SEX, TEACHER, PHONE,IDID,SITE,WAGE,IC,PASSWD from JIAN ")
        f = open(fr"C:\Xjian\teacher\{self.userSql}.txt", "w")
        for i in sun:
            string = f"工号：{i[0]} 姓名：{i[1]} 年龄：{i[2]} 性别：{i[3]} 类别：{i[4]} 电话：{i[5]} 身份证：{i[6]} 住址：{i[7]} 工资：{i[8]} 银行卡：{i[9]} 密码：{i[10]}"
            print(string)
            f.write(string + "\n")
        f.close()
        print("导出完成")

    def teacher(self):
        while True:
            f = open(r"C:\Xjian\Root\pwd.xjian", "r")
            passwd = f.readlines()
            self.passwd = passwd[0][:-1]
            f.close()
            print("""
            1，创建/删除 老师数据库
            2，添加老师信息
            3，删除老师信息
            4，修改老师信息
            5，查找老师信息
            6，导出所有老师信息
            7,退出
    """)
            dict1 = {"1": self.teacherSql, "2": self.addTeacher, "3": self.delTeacher, "4": self.amendTeacher,
                     "5": self.queryTeacher, "6": self.daochu}
            dict2 = {"1": "创建/删除 老师数据库",
                     "2": "添加老师信息",
                     "3": "删除老师信息",
                     "4": "修改老师信息",
                     "5": "查找老师信息",
                     "6": "导出所有老师信息",
                     "7": "退出"}

            userRoot = input("请输入序号：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} {dict2.get(userRoot)}")
            if userRoot == "7":
                return
            if not os.listdir(r"C:\Xjian\teacher") or userRoot == "1":
                sqlName = input("请输入数据库名字：")
                self.teacherSql(sqlName)
                continue
            name = dict1.get(userRoot, "-1")
            if name == "-1":
                continue
            print([i[:-3] for i in os.listdir(r"C:\Xjian\teacher")], "\n请选择数据库")
            userSql = input("请输入：")
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 选择数据库为：{userSql}")
            self.sql = rf"C:\Xjian\teacher\{userSql}.db"
            self.userSql = userSql
            name(3)
#
# A = Teacher()
# A.teacher()