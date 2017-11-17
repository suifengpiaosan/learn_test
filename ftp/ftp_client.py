# -*- coding: utf-8 -*-
# @Time    : 2017\11\16 0016 17:21
# @Author  : Rain
# @Email   : huaeryijiukai@gmail.com
# @File    : ftp_client.py
# @Software: PyCharm
import socket
client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input("cmd:").strip()
    client.send(cmd.encode("utf-8"))

    Racv_data = client.recv(8192)
    print(Racv_data.decode("utf-8"))
client.close()