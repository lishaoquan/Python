# -*- coding: utf-8 -*-
import random
import subprocess
from multiprocessing import Process

import time
from multiprocessing.pool import Pool

from Lib import os

# 获取当前进程的ID
print("current process id is %s" % os.getpid())


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# 创建进程执行任务
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print("Child process will start.")
    p.start()
    p.join()
    print("Child process end.")

print('***********************************************************')


# 创建多个进程，采用进程池的方式
def long_time_task(name):
    print('Run task %s(%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print("ALL subprocesses done.")

# 子进程的创建
print("$    nslookup www.python.org")
r = subprocess.call(['ping', 'www.python.org'])
print("ExitCode:", r)
