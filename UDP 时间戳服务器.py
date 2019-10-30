from socket import *
from time import ctime
'''
    HOST 和 PORT 变量与之前相同，原因与前面完全相同。对 socket()的调用的不同之
    处仅仅在于，我们现在需要一个数据报/UDP 套接字类型，但是 bind()的调用方式与 TCP
    服务器版本的相同。再一次，因为 UDP 是无连接的，所以这里没有调用“监听传入的
    连接”。
'''
Host=''
Port=21567
Bufsize=1024
Addr=(Host,Port)

udpsersock=socket(AF_INET,SOCK_DGRAM)
udpsersock.bind(Addr)
'''
    一旦进入服务器的无限循环之中，我们就会被动地等待消息（数据报）。当一条消息到达
    时，我们就处理它（通过添加一个时间戳），并将其发送回客户端，然后等待另一条消息。如
    前所述，套接字的 close()方法在这里仅用于显示。
'''
while True:
    print('waiting for message ')
    data,addr=udpsersock.recvfrom(Bufsize)
    print('from:',addr)
    udpsersock.sendto(b'[%s] %s'%(bytes(ctime(),'utf-8'),data),addr)

udpsersock.close()