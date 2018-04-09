# -*- coding: utf-8 -*-
# 序列化和反序列化
import json
import pickle

import time

from Lib import os

d = dict(name='lishaoquan', age=30, score=613, sex='男')
dump = pickle.dumps(d)
print(dump)
with open('F:\Python\study\dump.txt', 'wb') as file:
    file.write(dump)
with open("F:\Python\study\dump.txt", 'rb') as readfile:
    f = readfile.read()
    obj = pickle.loads(f)
    print(obj)
time.sleep(2)
os.remove("F:\Python\study\dump.txt")
print(json.dumps(d))
jsonfile = open("F:\Python\study\json.txt", 'w')
json.dump(d, jsonfile)
jsonfile.close()
readjsonfile = open("F:\Python\study\json.txt", 'r')
print(json.load(readjsonfile))


# 定义一个对象，然后使用json进行序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student("Bob", 33, 50)
jsonstr = json.dumps(s, default=lambda obj: obj.__dict__)
print(jsonstr)
print(json.loads(jsonstr, object_hook=dict2student))
