# -*- coding: utf-8 -*-
def add_end(L=[]):
    L.append("END")
    return L


print(add_end())
print(add_end([1, 2, 3]))
print(add_end())


def add_end_new(L=None):
    if L is None:
        L = []
    L.append("END")
    return L


print(add_end_new())
print(add_end_new())
print(add_end_new())


def person(name, age, *, sex):
    print("name:", name, ",age", age, ",sex:", sex)


person("Jim", 25, sex="male")


# 必选参数-可选参数-可变参数/命名关键字参数-关键字参数

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(4))
print(fact(10))


def move(ori, des):
    print("步骤:", ori, "--->", des)


def hanruota(n, a, b, c):
    if n == 1:
        move(a, c)
    else:
        hanruota(n - 1, a, c, b)
        move(a, c)
        hanruota(n - 1, b, a, c)


hanruota(2,'A','B','C')