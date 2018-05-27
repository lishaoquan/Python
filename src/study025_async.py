# coding=utf-8
import asyncio
import threading


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


def main01():
    c = consumer()
    produce(c)


@asyncio.coroutine
def hello_world():
    print("Hello,world!")
    yield from asyncio.sleep(10)
    print("Hello again!")


def main02():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())
    loop.close()


@asyncio.coroutine
def hello():
    print("Hello,world!%s" % threading.current_thread())
    yield from asyncio.sleep(1)
    print("Hello again! %s" % threading.current_thread())


def main03():
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


@asyncio.coroutine
def wget(host):
    print("wget from %s..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


def main04():
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.qq.com', 'www.sina.com', 'www.chd.com.cn']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    main04()
