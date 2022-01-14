#  @时间：2022/1/5  21:40
#  @作者：简词海
#  @代码名字：logs.py

def los(text):
    f = open(r"C:\Xjian\logs\los.lg", "a")
    f.write(text + "\n")
    f.close()
