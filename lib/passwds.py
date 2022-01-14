#  @时间：2022/1/7  20:15
#  @作者：简词海
#  @代码名字：passwds.py
str = False
a = False
b = False


def lens(lenst):
    global str, a, b
    if 16 >= len(lenst) >= 6:
        str = True
    for i in lenst:
        if i.isnumeric():
            a = True
    for j in lenst:
        if j.isalpha():
            b = True
    if str and a and b:
        return True


def mila(ma):
    if ma.find("@") != -1:
        return True
    else:
        return False
