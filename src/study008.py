# -*- coding: utf-8 -*-

'This is a test model'
import types

import math

__author__ = 'lishaoquan'

from PIL import Image
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello World! First args is %s" % args[0])
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")


if __name__ == "__main__":
    test()

_name = "test01"
__name = "test02"

im = Image.open("F:\\Python\\study\\temp\\logo.png")
print(im.format, im.size, im.mode)
im.thumbnail((50, 50))
im.save("F:\\Python\\study\\temp\\logo1.png", "PNG")
print(sys.path)


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s:%s" % (self.__name, self.__score))


stu1 = Student("Jim", 80)
stu2 = Student("Sam", 90)
stu1.print_score()
stu2.print_score()
stu1.__name = "Peter"
stu1.__score = 100
stu1.print_score()

print(type(123))
print(type("123"))
print(type(123.321))
print(type(None))
print(type(stu1))
print(type(sys))
print(type(abs))
print(type(pow) == types.FunctionType)
print(type(pow) == types.BuiltinFunctionType)
print(isinstance(abs, Student))
print(dir(str))

print(hasattr(stu1,"__name"))
print(hasattr(stu1,"sex"))
setattr(stu1,"sex","male")
print(hasattr(stu1,"sex"))
print(getattr(stu1,"sex"))
del stu1.sex
print(hasattr(stu1,"sex"))


