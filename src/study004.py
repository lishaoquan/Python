# -*- coding: utf-8 -*-
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sums = 0
for i in numbers:
    sums = sums + i
print(sums)
print(list(range(100)))
gaosi = 0
gaosilist = list(range(101))
for i in gaosilist:
    gaosi = gaosi + i
print("高斯:", gaosi)
# 100以内所有奇数之和
oddsum = 0
odd = 99
while odd > 0:
    oddsum = oddsum + odd
    odd = odd - 2
print(oddsum)
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print("Hello", i, "!")
d = {"name": "Peter", "age": 40, "sex": "male"}
print(d["age"])
d["age"] = 50
print(d["age"])
print("class" in d)
print("name" in d)
print(d.get("name"))
print(d.get("SEX"))
s = set([1, 2, 3, 4, 5, 3])
print(s)
print(abs(-100))
print(hex(255))


# 自定义函数
def my_abs(value):
    if not isinstance(value, (int, float)):
        raise TypeError("The type of param is wrong.")
    if value >= 0:
        return value
    else:
        return -value


#  练习


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        return "Param a is not a digit."
    if not isinstance(b, (int, float)):
        return "Param b is not a digit."
    if not isinstance(c, (int, float)):
        return "Param c is not a digit."
    delt = math.pow(b, 2) - 4 * a * c
    if delt < 0:
        return "No real root"
    elif delt == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b - math.sqrt(delt)) / (2 * a)
        x2 = (-b + math.sqrt(delt)) / (2 * a)
        return float(("%.2f" % x1)), float(("%.2f" % x2))


print(my_abs(-500))
print(my_abs(400))
print(quadratic(-5, 4, 2))
