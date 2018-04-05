# -*- coding: utf-8 -*-
from io import StringIO, BytesIO


def file01():
    a = open("E:/a.txt", 'r')
    sa = a.read()
    print(sa)
    a.close()


def file02():
    try:
        a = open("E:/a.txt", 'r')
        sa = a.read()
        print(sa)
    finally:
        if a:
            a.close()


def file03():
    with open("E:/a.txt", 'r') as a:
        sa = a.read()
        print(sa)


def readimage():
    image = open("F:/网站群分层图.png", 'rb')
    obj = image.read()
    print(obj)
    image.close()


def writefile():
    with open("E:/b.txt", "w", encoding="utf-8") as w:
        w.write("This is a test!\n")
        w.write("中文测试")


def operatestring():
    f = StringIO()
    f.write("Hello")
    f.write(" ")
    f.write("world!")
    print(f.getvalue())


def operatebyte():
    f = BytesIO()
    f.write("黎绍泉".encode("utf-8"))
    print(f.getvalue())



if __name__ == "__main__":
    operatestring()

