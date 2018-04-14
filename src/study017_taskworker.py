#  -*- coding: utf-8 -*-

import queue
import random
from multiprocessing.managers import BaseManager

import time


class QueueManager(BaseManager):
    pass


def task_worker():
    QueueManager.register("get_task_queue")
    QueueManager.register("get_result_queue")
    server_addr = '127.0.0.1'
    print("Connect to Server %s ...." % server_addr)
    manager = QueueManager(address=(server_addr, 5000), authkey=b"abc")
    manager.connect()
    # 通过网络访问注册到的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 从任务队列获取任务并把结果写到结果队列中
    for i in range(10):
        try:
            r = task.get(timeout=1)
            print("Run task %d..." % r)
            n = '%d*%d=%d' % (r, r, r * r)
            time.sleep(1)
            result.put(n)
        except queue.Queue.Empty:
            print("Task is Empty...")
    print("worker exit.")


if __name__ == "__main__":
    task_worker()
