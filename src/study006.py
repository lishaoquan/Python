# -*- coding: utf-8 -*-
from collections import Iterable
import os
from functools import reduce

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[0:10])
print(L[:10])
print(L[3:6])
L = list(range(100))
print(L[::5])
print(L[-10:])
print(L[:10:2])
print("ABCDEFG"[:4])
print(isinstance("ABC", Iterable))
print(isinstance(123456, Iterable))
for i, v in enumerate(["Jim", "Sam", "Peter"]):
    print(i, ":", v)
print([x * x for x in [1, 2, 3]])
print([x * x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 2 == 0])
print([d for d in os.listdir('F:\Python\study')])
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)


def test():
    yield 1
    yield 2
    yield 3


for i in test():
    print(i)


def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


n = 0
for i in triangles():
    print(i)
    n = n + 1
    if n == 5:
        break

print(abs)


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print(list(map(str, [1, 2, 3, 45, 6, 7, 8, 9])))


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))


def normalize(name):
    return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def pro(x, y):
    return x * y


print(reduce(pro, [1, 2, 3, 4, 5]))


