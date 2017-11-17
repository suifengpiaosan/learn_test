# -*- coding: utf-8 -*-
# @Time    : 2017\11\16 0016 17:21
# @Author  : Rain
# @Email   : huaeryijiukai@gmail.com
# @File    : ftp_server.py
# @Software: PyCharm
import socket,os
server = socket.socket()
server.bind(("localhost",9999))
server.listen()
while True:
     conn,addr=server.accept()
     data  = conn.recv(8192)
     Cmd_str = data.decode()
     cmd_linux =
     if Cmd_str is 'ls':
         Cmd_str = 'dir'
     print(Cmd_str)
     Result_data=os.popen(Cmd_str).read()

     conn.send(Result_data.encode("utf-8"))


server.close()