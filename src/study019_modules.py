# -*- coding: utf-8 -*-
import base64
import datetime

# datetime
import hashlib
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

import struct

import itertools
from urllib import request
from xml.parsers.expat import ParserCreate

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
dict = dict([("a", 1), ("b", 2), ("c", 3), ("a1", 4)])
print(dict)
orderdict = OrderedDict(dict)
print(orderdict)
# 统计字符出现的个数
c = Counter()
for i in "I am a promgrammer!":
    c[i] = c[i] + 1
print(c)
encodestr = base64.b64encode(b"str")
print(encodestr)
print(base64.b64decode(encodestr))


def safe_base64_decode(s):
    le = len(s)
    if (le % 4) != 0:
        l = le % 4
        strs = str(s, encoding="utf-8")
        for i in range(l):
            strs = strs + '='
        return base64.b64decode(bytes(strs, encoding="utf-8"))
    return base64.b64decode(s)


print(safe_base64_decode(encodestr))
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode(b'YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode(b'YWJjZA')
print('Pass')


# struct
def is_bit_pic(p):
    bpic = b""
    with open(p, "rb") as op:
        bpic = op.read(30)
    return struct.unpack('<ccIIIIIIHH', bpic)


print(is_bit_pic("F:\互联网组\红剑数据工厂\与领导驾驶舱融合/IMG_2599.PNG"))

# hashlib
md5 = hashlib.md5()
md5.update("This is updated by lishaoquan".encode("utf-8"))
print(md5.hexdigest())
md5.update("This is updated by wujiang".encode("utf-8"))
print(md5.hexdigest())
sha1 = hashlib.sha1()
sha1.update("This is updated by lishaoquan".encode("utf-8"))
print(sha1.hexdigest())
sha1.update("This is updated by wujiang".encode("utf-8"))
print(sha1.hexdigest())

# itertools
ns = itertools.repeat("ABC",3)
for i in ns:
    print(i)
for i in itertools.chain("ABC","XYZ"):
    print(i)
for key, group in itertools.groupby("AAABBBAAACCCA"):
    print(key,list(group))


# XML
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print("sax:start_element:%s,attrs:%s" % (name, str(attrs)))

    def char_data(self, text):
        print("sax:char_data:%s" % text)

    def end_element(self, name):
        print("sax:end_element:%s" % name)


xml = r"""<?xml version="1.0"?>
<ol>
<li><a href="/python">Python</a></li>
<li><a href="/ruby">Ruby</a></li>
</ol>
"""
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
    data = f.read();
    print("Status:", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s:%s" % (k, v))
    print("Data:", data.decode("utf-8"))

req = request.Request("http://www.baidu.com/s?wd=Java")
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
