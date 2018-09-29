import socket
'''socket编程'''
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      # 买手机
#socket.AF_INET-基础网络通信
phone.bind(('127.0.0.1',8000))                              # 绑定

phone.listen(5)                                             #监听，半链接池

