# -*- coding: utf-8 -*-
import logging

import unittest2 as unittest2

logging.basicConfig(level=logging.INFO)
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                       'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)
for name, member in Month.__members__.items():
    print(name, "->", member, "->", member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Sun)
print(Weekday["Sun"])
print(Weekday.Sun.value)
print(Weekday(0))
print(type(Weekday))


def fn(self, name="world"):
    print("Hello,%s" % name)


Hello = type("Hello", (object,), dict(hello=fn))
h = Hello()
h.hello("Mikkey")


def delete(self, v):
    self.remove(v)
    return self


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        attrs["delete"] = delete
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.append("A")
print(L)
L.append("B")
print(L)
L.delete("A")
print(L)

try:
    1 / 0
except Exception as e:
    print("错误:", e)
finally:
    print("finally block...")

logging.info("这个是一个日志记录的工具!")


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value %s" % n)
    return n


# foo("0")


def aaa(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def bbb():
    aaa("0")


# bbb()


class MyDict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute'%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


class TestMyDict(unittest2.TestCase):

    def setUp(self):
        print("setup...")

    def tearDown(self):
        print("teardown...")

    def test_init(self):
        d = MyDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = MyDict();
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest2.main()