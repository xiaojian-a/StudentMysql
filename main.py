#  @时间：2022/1/1  21:41
#  @作者：简词海
#  @代码名字：main.py

import os
import lib.OsMkdir as mk
import lib.pwd as pwd
import lib.user as rus
import time
import lib.logs as lo

def main():
    if not os.path.exists(r"C:\Xjian"):
        mk.mkdir()
    while True:
        print("""
            ============================
                   欢迎使用学生管理系统
                   1、root登录（忘记密码输入q）
                   2、老师登录
                   3、学生登录
                   4、退出
            ============================
        """)
        user = input("请选择输入序号：")
        if user == "q":
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 忘记密码，准备修改密码")
            pwd.passwd()
        elif user == "1":
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} root正在登录")
            rus.rootUser()
        elif user == "2":
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 老师正在登录")
            rus.teacherUser()
        elif user == "3":
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 学生正在登录")
            rus.studentUser()
        elif user == "4":
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 退出系统")
            print("欢迎下次使用")
            break
        else:
            print("请正确输入")


if __name__ == "__main__":
    main()
