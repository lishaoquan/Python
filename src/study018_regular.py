# -*- coding: utf-8 -*-
import re

print(re.match(r'\d{10}', "lishaoquan"))
print(re.match(r'\w{10}', "lishaoquan"))
print(re.split(r'\s+', "a b  c"))
# 定义提取电话号码的区号和号码的正则
r = r'^(\d{3})-(\d{5,8})$';
m = re.match(r, "025-65533")
if m:
    print(m.group(1), ",", m.group(2))
else:
    print("未匹配.")
print(re.match(r'^(\d+)(0*)$', "12305000").groups())
print(re.match(r'^(\d+?)(0*)$', "12305000").groups())
# 预编译正则
telphone_re = re.compile(r)
print(telphone_re.match("010-83564459").groups())
print(telphone_re.match("025-4356788").groups())
# 验证email的正则
email_re = re.compile(r'^(<(\w*\s*\w*)>)?\s*(\w+.?\w+)@\w+(.com|.org)$')
print(email_re.match("<zhang  san> lishaoquan@huawei.com").groups())
print(email_re.match("lishaoquan@huawei.com").groups())
print(email_re.match("leo.lishaoquan@huawei.com").groups())
