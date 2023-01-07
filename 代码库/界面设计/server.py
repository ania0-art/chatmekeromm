'''
Author: ania0-art 75117340+ania0-art@users.noreply.github.com
Date: 2022-12-28 17:05:54
LastEditors: ania0-art 75117340+ania0-art@users.noreply.github.com
LastEditTime: 2022-12-29 15:05:50
FilePath: \程序设计\代码库\界面设计\server.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import socket
import threading

#创建tcp socket,类型为服务器之间网络通信，流式socket
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定服务器ip和端口
mySocket.bind(("localhost",2345))
# 开始监听tcp传入连接，并设置操作系统可以挂起的最大连接数
mySocket.listen(5)

print('Server was started by',socket.gethostbyname('localhost'),'now is listening')
# 创建字典，用于存储客户端的用户
mydict = dict()
# 创建列表，用于存储客户端连接
mylist = list()

# 把聊天信息发送给除自己以外所有人
def chatMsgToOthers(exceptMe,chatMsg):
    for c in mylist:
        if c.fileno() != exceptMe:
            try:
                # 向客户端发送信息
                c.send(chatMsg.encode())
            except:
                pass

# 保持与客户端连接的子线程的处理逻辑
def subThreadProcess(myconnection,connNum):
    # 接收客户端消息
    username = myconnection.recv(1024).decode()
    mydict[myconnection.fileno()] = username
    mylist.append(myconnection)
    print('client connection number:',connNum,'has nickname',username)
    while True:
        try:
            # 接收客户端消息
            recvedMsg = myconnection.recv(1024).decode()
            if recvedMsg:
                print(mydict[connNum],':',recvedMsg)
                chatMsgToOthers(connNum,recvedMsg)
        except(OSError,ConnectionResetError):
            try:
                mylist.remove(myconnection)
            except:
                pass
            print(mydict[connNum],'was exit, ',len(mylist),'person left')
            chatMsgToOthers(connNum,mydict[connNum]+' 已经离开聊天室')
            myconnection.close()
            return

while True:
    # 接受tcp连接并返回（connection,address),connection是新的socket对象，用来接收和发送数据，address是连接客户端的地址
    connection,address=mySocket.accept()
    print('Accept a new connection',connection.getsockname(),connection.fileno())
    try:
        # 接收客户端消息
        buf = connection.recv(1024).decode()
        if buf == '1':
            # 向客户端发送消息
            connection.send(b'connection success,welcome to chat room')
            # 为当前连接创建一个新的子线程来保持通信
            myThread = threading.Thread(target=subThreadProcess,args=(connection,connection.fileno()))
            myThread.setDaemon(True)
            myThread.start()
        else:
            # 向当前客户端发送信息
            connection.send(b'connection fail, please go out')
            connection.close()
    except:
        pass