#  @时间：2022/1/1  22:36
#  @作者：简词海
#  @代码名字：pwd.py
import time
import lib.passwds
import lib.mail
import hashlib
import lib.logs as lo


def passwd_g(mails, userWd):
    userPsswd1 = input("请输入修改后的密码")
    userPsswd2 = input("请再次输入修改后的密码")
    if userPsswd1 == userPsswd2:
        if passwds.lens(userPsswd1):
            m1 = hashlib.md5()
            m1.update(userPsswd2.encode(encoding='utf-8'))
            f1 = open(r"C:\Xjian\Root\pwd.xjian", "w")
            f1.write(f"{m1.hexdigest()}\n{mails}\n{userWd}")
            f1.close()
        else:
            print("密码输入强度不够")
    else:
        print("两次密码不同，请重新输入")


def passwd():
    while True:
        print("选择找回密码的方式：1、邮箱验证码  2 、安全问题")
        user = input("请选择输入：")
        if user == "1":
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 忘记密码，正在以邮箱的形式找回密码")
            f = open(r"C:\Xjian\Root\pwd.xjian", "r")
            file = f.readlines()
            mails = file[1][:-1]
            userWd = file[2][:-1]
            f.close()
            user_mail = input("请输入安全邮箱：")
            m = hashlib.md5()
            m.update(user_mail.encode(encoding="utf-8"))
            if m.hexdigest() == mails:
                age = lib.mail.Mail(user_mail).mails()
                userAge = input("请输入验证码:")
                if userAge == age:
                    passwd_g(mails, userWd)
                    lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 忘记密码，正在以邮箱的形式更改密码成功")
                else:
                    print("验证码输入错误")
            else:
                print("邮箱输入错误，请检查后重新输入")
        elif user == "2":
            lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 忘记密码，正在以安全问题的形式找回密码")
            f = open(r"C:\Xjian\Root\pwd.xjian", "r")
            file = f.readlines()
            print(file)
            mails = file[1][:-1]
            userWd = file[2][:-1]
            list_file = file[2].split("=")
            print("安全问题是：", list_file[0])
            user_file = input("请输入答案：")
            m = hashlib.md5()
            m.update(user_file.encode(encoding="utf-8"))
            if m.hexdigest() == list_file[1]:
                passwd_g(mails, userWd)
                lo.los(f"时间：{time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())} 忘记密码，正在以安全问题的形式更改密码成功")
            else:
                print("安全问题答案错误，请重新输入")

        else:
            return
