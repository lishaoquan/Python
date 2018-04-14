#  -*- coding: utf-8 -*-

# 创建发送任务的队列和接受任务的队列
import queue
import random
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


def task_queue_fun():
    global task_queue
    return task_queue


def result_queue_fun():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
    pass


def task_master():
    # 把发送任务队列和接受任务注册到网络上
    QueueManager.register("get_task_queue", callable=task_queue_fun)
    QueueManager.register("get_result_queue", callable=result_queue_fun)
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b"abc")
    manager.start()
    # 通过网络访问注册到的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print("Put task %d..." % n)
        task.put(n)
    # 读取结果
    print("Try get results ...")
    for i in range(10):
        r = result.get(timeout=10)
        print("Result: %s" % r)
    manager.shutdown()
    print("Master exit.")


if __name__ == "__main__":
    task_master()
