# -*- coding: utf-8 -*-
import multiprocessing
import random
import subprocess
import threading
from multiprocessing import Process, Queue

import time
from multiprocessing.pool import Pool

from Lib import os


# 进程间通信
# 写进程执行的方法
def write(q):
    print("Process to write: %s" % os.getpid())
    for v in ['A', 'B', 'C']:
        print("Put %s to queue." % v)
        q.put(v)
        time.sleep(random.random() * 3)


# 读进程执行的方法
def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get from queue : %s " % value)


# 模拟生产者和消费者
def main1():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


# 打印输出线程
def printthread():
    print("Thread is running:%s" % threading.currentThread().name)
    time.sleep(3)
    print("Thread is end:%s" % threading.currentThread().name)


# 通过threading创建线程
def main2():
    print("Thread is running:%s" % threading.current_thread().name)
    t = threading.Thread(target=printthread, name='PrintThread')
    t.start()
    t.join()
    print("Thread is end:%s" % threading.currentThread().name)


# 银行存款的例子
balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    lock.acquire()
    try:
        for i in range(100000):
            change_it(n)
    finally:
        lock.release()


def main3():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


local_std = threading.local()


class Student(object):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("Thread %s process Student name is %s" % (threading.current_thread().name, self.name))


def process_student():
    std = local_std.student
    std.print()


def process_thread(name):
    std = Student(name)
    local_std.student = std
    process_student()


def main4():
    t1 = threading.Thread(target=process_thread, args=("lishaoquan",), name="A")
    t2 = threading.Thread(target=process_thread, args=("zhangsan",), name="B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    # main1()
    # main2()
    # main3()
    # print(multiprocessing.cpu_count())
    # main4()
    pass
