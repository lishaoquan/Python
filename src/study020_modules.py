# -*- coding: utf-8 -*-
import socket

# 客户端
import threading

import time


def conn_sina():
    # 创建socket连接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    s.connect(("www.sina.com", 80))
    print("已经建立与新浪的连接.", s.getsockname())
    # 发送数据:
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')
    buffer = []
    while True:
        # 每次最多接收 1k 字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    s.close()
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open("F:/Python/study/sina.html", 'wb') as  f:
        f.write(html)


def tcplink(sock, addr):
    print("Accept new conection from %s:%s..." % addr)
    sock.send(b"Welcome")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8") == "exit":
            break
        sock.send(("Hello,%s !" % data).encode("utf-8"))
    sock.close()
    print("Conection from %s:%s is closed." % addr)


def server_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 9999))
    s.listen(5)
    print("Waiting for connection...")
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


if __name__ == "__main__":
    server_socket()
