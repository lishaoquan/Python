# -*- coding: utf-8 -*-
import math

import functools


def is_odd(x):
    return x % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 给一个数字，判断是不是素数
def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


print(is_prime(10))
print(is_prime(11))
print(is_prime(13))
print(is_prime(15))
print(is_prime(25))
print(is_prime(37))


# 判断一个数是不是回数
def is_backunmber(n):
    positivestr = str(n)
    negetivestr = ''
    strlen = len(positivestr)
    for i in range(1, strlen + 1):
        negetivestr += positivestr[-i]
    return positivestr == negetivestr


print(list(filter(is_backunmber, range(1000, 2000))))

L = [1, 2, 36, 6, 9, 3, 67, -24]
print(L)
print(sorted(L))
print(sorted(L, key=abs))


def get_digit(t):
    return t[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L))
print(sorted(L, key=lambda t: t[1]))
print(sorted(L, key=get_digit))


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("begin call %s()" % func.__name__)
        func(*args, **kw)
        print("end call %s()" % func.__name__)

    return wrapper


@log
def test():
    print("test")


test()

int2 = functools.partial(int, base=2)
print(int2("011"))
