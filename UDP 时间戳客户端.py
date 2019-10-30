from socket import *
'''
    因为这次还是在本地计算机上运行服务器，所以使用“localhost”及与客户端相同的
    端口号，并且缓冲区大小仍旧是 1KB。另外，以与 UDP 服务器中相同的方式分配套接字
    对象。
'''
Host='127.0.0.1'
Port=21567
Bufsize=1024
Addr=(Host,Port)
'''
    UDP 客户端循环工作方式几乎和 TCP 客户端完全一样。唯一的区别是，事先不需要建
    立与 UDP 服务器的连接，只是简单地发送一条消息并等待服务器的回复。在时间戳字符串返
    回后，将其显示到屏幕上，然后等待更多的消息。最后，当输入结束时，跳出循环并关闭套
    接字。
'''
udpserSock=socket(AF_INET,SOCK_DGRAM)
while True:
    data=input('> ')
    if not data:
        break
    udpserSock.sendto(data.encode(),Addr)
    data,addr=udpserSock.recvfrom(Bufsize)
    if not data:
        break
    print(data.decode())