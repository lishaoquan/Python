# -*- coding: utf-8 -*-
import math

classmates = ["Jim", "Jam", "Peter", "Smith"]
print(classmates)
print(len(classmates))
print(classmates[2])
# -1表示最后一个元素d的索引
print(classmates[-1])
classmates.append("Sam")
print(classmates)
classmates.insert(4, "Kin")
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)
tuples = (123, 456)
print(tuples)
tuples = (1, 2, 3, [4, 5])
print(tuples)
tuples[3][0] = "A"
tuples[3][1] = "B"
print(tuples)
# 练习
L = [
 ['Apple', 'Google', 'Microsoft'],
 ['Java', 'Python', 'Ruby', 'PHP'],
 ['Adam', 'Bart', 'Lisa']
]
# 打印 Apple:
print(L[0][0])
print(L[-3][-3])
# 打印 Python:
print(L[1][1])
print(L[-2][-3])
# 打印 Lisa:
print(L[2][2])
print(L[-1][-1])
# 条件判断
age = 20
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenage")
else:
    print("kid")
s = input("请输入您出生的年份:")
if not s:
    s = input("请输入您出生的年份:")
year = int(s)
if year >= 2000:
    print("00后")
elif year >= 1980:
    print("80和90后")
else:
    print("70后以前")
# 练习
height = 1.75
weight = 80.5
bmi = weight/(math.pow(height, 2))
bmi = float(("%.1f" % bmi))
print("您的BMI指数是：", bmi)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi <= 25:
    print("正常")
elif 25 < bmi <= 28:
    print("过重")
elif 28 < bmi <= 32:
    print("肥胖")
else:
    print("严重肥胖")

