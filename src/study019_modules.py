# -*- coding: utf-8 -*-

import datetime

# datetime
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

now = datetime.datetime.now()
print(now)
print(type(now))
ts = now.timestamp()
print(ts)
print(datetime.datetime.fromtimestamp(ts))
str1 = "2018-4-12 15:43:9"
print(datetime.datetime.strptime(str1, "%Y-%m-%d %H:%M:%S"))
print(now.strftime("%a, %b %d %H:%M"))
yesterday = now - datetime.timedelta(days=1)
print(yesterday)
tomorrow = now + datetime.timedelta(days=1)
print(tomorrow)


def to_timestamp(dt_str, tz_str):
    dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    tz = datetime.timezone(datetime.timedelta(hours=int(tz_str)))
    newdt = dt.replace(tzinfo=tz)
    return newdt.timestamp()


print(to_timestamp("2018-12-12 12:34:56", "8"))
t1 = to_timestamp('2015-6-1 08:10:30', '7')
assert t1 == 1433121030.0, t1
print("Pass")

# collections
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)
d = deque(["a", "b", "c"])
d.append("d")
print(d)
d.appendleft("e")
print(d)
dd = defaultdict(lambda: "NAN")
dd["key1"] = "Hello"
print(dd["key1"])
print(dd["key2"])
dict = dict([("a",1),("b",2),("c",3),("a1",4)])
print(dict)
orderdict = OrderedDict(dict)
print(orderdict)
# 统计字符出现的个数
c = Counter()
for i in "I am a promgrammer!":
    c[i] = c[i] + 1
print(c)
