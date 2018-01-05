# -*- coding: utf-8 -*-
print(ord('A'))
print(ord('B'))
print(chr(68))
print("你好".encode('utf-8'))
print('Hello'.encode('ascii'))
print(b"Welcome".decode('ascii'))
print(len('你好啊!'))
print(len('Hello man!'))
print("你好,%s,欢迎来到%s世界!你有%d块钱吗?" % ('黎绍泉',  '侏罗纪',  300))
# 练习
lastYearScore = 72
thisYearScore = 85
percent = (thisYearScore - lastYearScore) / lastYearScore
print("恭喜你,你的成绩提升了%.1f%%" % percent)




