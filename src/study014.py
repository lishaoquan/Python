# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime

print(os.name)
print(os.environ)
print(os.environ.get("PATH"))
print(os.path.abspath('.'))
newdir = os.path.join('F:\Python\study', 'new')
print(newdir)
if not os.path.exists(newdir):
    os.mkdir(newdir)
# 文件夹创建后，休眠2s在进行删除，可以看到创建的过程
time.sleep(2)
os.rmdir(newdir)
print(os.path.split(newdir))
print(os.path.split('F:\Python\study\python362.chm'))
print(os.path.splitext('F:\Python\study\python362.chm'))
# 对文件进行操作：重命名，删除
with open('F:/Python/study/test.txt', 'w', encoding='utf-8') as file:
    file.write("test")
time.sleep(2)
os.rename('F:/Python/study/test.txt', 'F:/Python/study/test01.txt')
time.sleep(2)
os.remove('F:/Python/study/test01.txt')
# 列出指定目录下的所有文件夹和文件
print([x for x in os.listdir('F:/Python/study')])
# 对上面过滤出所有文件夹
print([x for x in os.listdir('F:/Python/study') if os.path.isdir(os.path.join('F:/Python/study', x))])
#  过滤出所有的pdf格式文件
print([x for x in os.listdir('F:/Python/study') if os.path.isfile(os.path.join('F:/Python/study', x))
       and os.path.splitext(os.path.join('F:/Python/study', x))[1] == '.pdf'])
# 写一个输出当前目录下的文件和目录的程序，并列出文件目录的大小，最近修改时间
current = os.path.abspath('.')
print("模拟命令dir -l:")
print("  Size             Last Modified                       Name")
print('------------------------------------------------------------------')
pwd = os.listdir(current)
for i in pwd:
    real = os.path.join(current, i)
    size = os.path.getsize(real)
    mtime = datetime.fromtimestamp(os.path.getmtime(real)).strftime('%Y/%m/%d %H:%M')
    if os.path.isdir(real):
        print('%5d              %s             %s%s ' % (size, mtime, i, '/'))
    else:
        print('%5d            %s             %s%s ' % (size, mtime, i, ''))
