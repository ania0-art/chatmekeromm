'''
Author: ania0-art 75117340+ania0-art@users.noreply.github.com
Date: 2022-12-27 14:19:47
LastEditors: ania0-art 75117340+ania0-art@users.noreply.github.com
LastEditTime: 2023-01-07 18:40:47
FilePath: \程序设计\代码库\界面设计\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pymysql
import tkinter as tk
import functools
import tkinter.ttk as ttk
import datetime
import socket
import threading
import tkinter.messagebox 

#创建tcp socket,类型为服务器之间网络通信，流式socket
client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立通信
client_sock.connect(("localhost",2345))
# 发送请求连接
client_sock.send(b'1')
# 从服务器接收到消息
print(client_sock.recv(1024).decode())

# 连接到 MySQL 数据库
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="usechat",
    port=8888
)
cursor = conn.cursor()

class client:
    def __init__(self,root):
        self.root=root
        self.root.title("慰藉深夜每一个孤独而又寂寞的灵魂")
        self.root.geometry("500x250")
        #载入图片
        self.image=tk.PhotoImage(file="代码库\界面设计\\1.gif")
        self.label_root=tk.Label(self.root,image=self.image)
        #创建跳转按钮
        self.button = tk.Button(self.root, text="点击开启您的神秘之旅吧", command=self._login_windows)
        self.button.pack(side="bottom")
        self.label_root.pack()

    # 登录窗口
    def _login_windows(self):
        self.root.withdraw()
        self.login_windows=tk.Toplevel(self.root)
        self.login_windows.title("登陆界面")
        self.login_windows.geometry("500x250")

        # 创建用户名输入框和密码输入框
        self.username_label_login = tk.Label(self.login_windows, text="用户名：")
        self.username_entry_login = tk.Entry(self.login_windows)
        self.password_label_login = tk.Label(self.login_windows, text="密码：")
        self.password_entry_login = tk.Entry(self.login_windows, show="*")
        # 创建提示信息标签
        # self.label_login = tk.Label(self.login_windows)
        #创建关闭按钮，登录按钮，注册按钮
        self.login_button = tk.Button(self.login_windows, text="登录", command=self.login)
        self.close_button = tk.Button(self.login_windows, text="关闭", command=self.close_all)
        self.comeback_button = tk.Button(self.login_windows, text="返回", command=functools.partial(self.goback,self.login_windows,self.root))
        self.signup_button = tk.Button(self.login_windows,text="没有账户，点击注册",command=self._sign_windows)
        self.username_label_login.pack()
        self.username_entry_login.pack()
        self.password_label_login.pack()
        self.password_entry_login.pack()
        self.login_button.pack()
        self.close_button.pack()
        self.comeback_button.pack()
        self.signup_button.pack()
        # self.label_login.pack()

    # 登录函数
    def login(self):
        # 获取用户名和密码
        self.username = self.username_entry_login.get()
        self.password = self.password_entry_login.get()

        # 执行 SQL 查询，检查用户名和密码是否正确
        cursor.execute(f"SELECT * FROM USER_LOGIN WHERE QQ_NO='{self.username}' AND PASSWORD='{self.password}'")
        result = cursor.fetchone()
        if result:
            # 如果用户名和密码正确，显示登录成功信息
            # self.label_login.config(text="登录成功！")
            tkinter.messagebox.showinfo('提示','登录成功！')
            self._homepage(result[0])
        else:
            # 如果用户名或密码错误，显示错误信息
            # self.label_login.config(text="用户名或密码错误，请重试！")
            tkinter.messagebox.showinfo('提示','用户名或密码错误，请重试！')

    # 注册窗口
    def _sign_windows(self):
        self.login_windows.withdraw()
        self.sign_windows=tk.Toplevel(self.root)
        self.sign_windows.title("注册界面")
        self.sign_windows.geometry("500x500")

        # 创建用户名输入框、密码输入框、确认密码,性别，年龄输入框
        self.nickname_label = tk.Label(self.sign_windows,text="请输入用户名：")
        self.nickname_entry = tk.Entry(self.sign_windows)
        self.entry_var = tk.StringVar()
        self.username_label = tk.Label(self.sign_windows, text="账号：")
        self.username_entry = tk.Entry(self.sign_windows,textvariable=self.entry_var)
        self.entry_var.set("请输入八位数")
        self.password_label = tk.Label(self.sign_windows, text="密码：")
        self.password_entry = tk.Entry(self.sign_windows, show="*")
        self.password_confirm_label = tk.Label(self.sign_windows, text="确认密码：")
        self.password_confirm_entry = tk.Entry(self.sign_windows, show="*")
        self.gender_label = tk.Label(self.sign_windows,text="请输入性别：")
        self.gender_entry = tk.Entry(self.sign_windows)
        self.age_label = tk.Label(self.sign_windows,text="请输入年龄：")
        self.age_entry = tk.Entry(self.sign_windows)
        self.telephone_label = tk.Label(self.sign_windows,text="请输入电话：")
        self.telephone_entry = tk.Entry(self.sign_windows)
        

        # 创建提示信息标签
        # self.label_sign = tk.Label(self.sign_windows)
        #创建关闭按钮，注册按钮，返回按钮
        self.close_button = tk.Button(self.sign_windows, text="关闭", command=self.close_all)
        self.comeback_button = tk.Button(self.sign_windows, text="返回", command=functools.partial(self.goback,self.sign_windows,self.login_windows))
        self.signup_button = tk.Button(self.sign_windows,text="注册",command=self.signup)
        self.close_button.pack(side="bottom")
        self.comeback_button.pack(side="bottom")
        self.signup_button.pack(side="bottom")
        self.nickname_label.pack()
        self.nickname_entry.pack()
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.password_confirm_label.pack()
        self.password_confirm_entry.pack()
        self.gender_label.pack()
        self.gender_entry.pack()
        self.age_label.pack()
        self.age_entry.pack()
        self.telephone_label.pack()
        self.telephone_entry.pack()
        #self.label_sign.pack()

    # 注册函数
    def signup(self):
        # 获取用户名、密码、确认密码
        self.nickname = self.nickname_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.telephone = self.telephone_entry.get()
        self.password_confirm = self.password_confirm_entry.get()
        self.gender = self.gender_entry.get()
        self.age = self.age_entry.get()

        # 判断密码是否一致
        if self.password != self.password_confirm:
            #self.label.config(text="两次输入的密码不一致！")
            tkinter.messagebox.showinfo('提示','两次输入的密码不一致！')
            return

        # 判断用户名是否已存在
        cursor.execute(f"SELECT * FROM USER_LOGIN WHERE QQ_NO='{self.username}'")
        result = cursor.fetchone()
        if result:
            #self.label_sign.config(text="用户名已存在！")
            tkinter.messagebox.showinfo('提示','账号已存在！')
            return

        # 判断账号，密码，年龄，昵称，电话号码，性别是否为空
        if len(self.username)==0:
            tkinter.messagebox.showinfo('提示','账号不能为空')
            return
        if len(self.password) ==0:
            tkinter.messagebox.showinfo('提示','密码不能为空')
            return
        if len(self.age) == 0:
            tkinter.messagebox.showinfo('提示','年龄不能为空')
            return
        if len(self.nickname) == 0:
            tkinter.messagebox.showinfo('提示','昵称不能为空')
            return
        if len(self.telephone) ==0:
            tkinter.messagebox.showinfo('提示','电话不能为空')
            return
        if len(self.gender) == 0:
            tkinter.messagebox.showinfo('提示','性别不能为空')
            return

        # 账号校验 八位纯数字
        if (not self.username.isdigit()) or len(self.username) != 8:
            tkinter.messagebox.showinfo('提示','账号为八位纯数字')
            return
        
        #密码校验，数字和字母的组合
        if self.password.isdigit():
            tkinter.messagebox.showinfo('提示','密码应该为数字和字母的组合')
            return
            
        #电话校验，十一位数字
        if (not self.telephone.isdigit()) or len(self.telephone) !=11:
            tkinter.messagebox.showinfo('提示','电话应该为十一位数字')
            return

        # 插入新用户
        cursor.execute(f"INSERT INTO USER_LOGIN (QQ_NO, PASSWORD) VALUES ('{self.username}', '{self.password}')")
        cursor.execute(f"INSERT INTO USER_INFO (QQ_NO,NICKNAME,GENDER,AGE,TELEPHONE) VALUES ('{self.username}', '{self.nickname}','{self.gender}','{self.age}','{self.telephone}')")
        conn.commit()

        # 注册成功，显示提示信息
        # self.label_sign.config(text="注册成功！")
        tkinter.messagebox.showinfo('提示','注册成功！点击返回按钮进入登录界面登录')

    # 定义个人主页函数
    def _homepage(self,id):
        self.login_windows.withdraw()
        #创建notebook组件
        self.homepage=tk.Toplevel(self.root)
        self.homepage.title("个人主页")
        self.homepage.geometry("500x500")
        self.notebook = ttk.Notebook(self.homepage)
        self.id=id
        #创建个人信息页面
        self.result=self.get_info()
        self.info_frame = tk.Frame(self.notebook)
        self.usename_label = tk.Label(self.info_frame, text='账号：')
        self.usename_entry = tk.Entry(self.info_frame)
        self.name_label = tk.Label(self.info_frame, text='用户名：')
        self.name_entry = tk.Entry(self.info_frame)
        self.gender_label = tk.Label(self.info_frame, text='性别：')
        self.gender_entry = tk.Entry(self.info_frame)
        self.age_label = tk.Label(self.info_frame, text='年龄：')
        self.age_entry = tk.Entry(self.info_frame)
        self.telephone_label = tk.Label(self.info_frame, text='电话：')
        self.telephone_entry = tk.Entry(self.info_frame)
        #数据插入
        self.usename_entry.insert(0,self.result[0])
        self.name_entry.insert(0,self.result[1])
        self.gender_entry.insert(0,self.result[2])
        self.age_entry.insert(0,self.result[3])
        self.telephone_entry.insert(0,self.result[4])
        #布局
        self.usename_label.pack()
        self.usename_entry.pack()
        self.name_label.pack()
        self.name_entry.pack()
        self.gender_label.pack()
        self.gender_entry.pack()
        self.age_label.pack()
        self.age_entry.pack()
        self.telephone_label.pack()
        self.telephone_entry.pack()

        self.close_button = tk.Button(self.info_frame, text="关闭", command=self.close_all)
        self.close_button.pack(side="bottom")
        self.change_button = tk.Button(self.info_frame,text="修改资料",command=self._change_windows)
        self.change_button.pack()
        # 创建好友列表页面
        self.friends_frame = tk.Frame(self.notebook)
        self.close_button = tk.Button(self.friends_frame, text="关闭", command=self.close_all)
        self.close_button.grid(row=6,column=0)
        self.friends_label = tk.Label(self.friends_frame,text="请输入想要添加或者删除好友的账号")
        self.friends_entry = tk.Entry(self.friends_frame)
        self.friends_label.grid(row=2,column=0)
        self.friends_entry.grid(row=3,column=0)
        # 添加或者删除好友
        self.add_friedns_button = tk.Button(self.friends_frame,text='添加好友',command=self.addfriends)
        self.add_friedns_button.grid(row=4,column=0)
        self.delete_friedns_button = tk.Button(self.friends_frame,text='删除好友',command=self.deletefriends)
        self.delete_friedns_button.grid(row=5,column=0)
        # 显示好友数量
        self.friend_count_label = tk.Label(self.friends_frame, text=f"好友数量：{self.get_friend_count()}")
        self.friend_count_label.grid(row=0, column=0)
        # 创建列表框
        self.friend_names_listbox = tk.Listbox(self.friends_frame)
        # 将好友名字添加到列表框中
        for name in self.get_friend_names():
            self.friend_names_listbox.insert(tk.END, name)
        #绑定回调函数
        self.friend_names_listbox.bind('<<ListboxSelect>>', self.on_select)
        # 显示列表框
        self.friend_names_listbox.grid(row=1,column=0)

        # 将页面添加到 Notebook 组件中
        self.notebook.add(self.info_frame, text='个人信息')
        self.notebook.add(self.friends_frame, text='好友列表')
        
        # 显示 Notebook 组件
        self.notebook.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    # 定义修改个人资料的函数窗口
    def _change_windows(self):
        self.change_windows=tk.Toplevel(self.root)
        self.change_windows.title("修改界面")
        self.change_windows.geometry("500x500")

        # 创建用户名输入框、密码输入框、确认密码,性别，年龄输入框
        self.nickname_label = tk.Label(self.change_windows,text="请输入新的用户名：")
        self.nickname_entry = tk.Entry(self.change_windows)
        self.password_label = tk.Label(self.change_windows, text="新的密码：")
        self.password_entry = tk.Entry(self.change_windows, show="*")
        self.password_confirm_label = tk.Label(self.change_windows, text="确认新的密码：")
        self.password_confirm_entry = tk.Entry(self.change_windows, show="*")
        self.gender_label = tk.Label(self.change_windows,text="请输入性别：")
        self.gender_entry = tk.Entry(self.change_windows)
        self.age_label = tk.Label(self.change_windows,text="请输入年龄：")
        self.age_entry = tk.Entry(self.change_windows)
        self.telephone_label = tk.Label(self.change_windows,text="请输入电话：")
        self.telephone_entry = tk.Entry(self.change_windows)  
        self.nickname_entry.insert(0,self.result[1])
        self.gender_entry.insert(0,self.result[2])
        self.age_entry.insert(0,self.result[3])
        self.telephone_entry.insert(0,self.result[4]) 
        # 修改按钮
        self.change_button_ = tk.Button(self.change_windows,text="确认修改",command=self.change)
        # 布局
        self.nickname_label.pack()
        self.nickname_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.password_confirm_label.pack()
        self.password_confirm_entry.pack()
        self.gender_label.pack()
        self.gender_entry.pack()
        self.age_label.pack()
        self.age_entry.pack()
        self.telephone_label.pack()
        self.telephone_entry.pack()
        self.change_button_.pack()
    
    # 定义修改个人资料的函数
    def change(self):
        # 获取用户名、密码、确认密码
        self._nickname = self.nickname_entry.get()
        self._password = self.password_entry.get()
        self._telephone = self.telephone_entry.get()
        self._password_confirm = self.password_confirm_entry.get()
        self._gender = self.gender_entry.get()
        self._age = self.age_entry.get()
        
        try:
            # 判断密码是否一致
            if self._password != self._password_confirm:
                #self.label.config(text="两次输入的密码不一致！")
                tkinter.messagebox.showinfo('提示','两次输入的密码不一致！')
                return

            #密码校验，数字和字母的组合
            if self._password.isdigit():
                tkinter.messagebox.showinfo('提示','密码应该为数字和字母的组合')
                return
                
            #电话校验，十一位数字
            if (not self._telephone.isdigit()) or len(self._telephone) !=11:
                tkinter.messagebox.showinfo('提示','电话应该为十一位数字')
                return

            # 更新用户
            cursor.execute(f"UPDATE USER_LOGIN SET PASSWORD= '{self._password}' WHERE QQ_NO='{self.username}'")
            cursor.execute(f"UPDATE USER_INFO SET NICKNAME='{self._nickname}',GENDER='{self._gender}',AGE='{self._age}',TELEPHONE='{self._telephone}' WHERE QQ_NO='{self.username}'")
            conn.commit()

            # 修改成功，显示提示信息
            tkinter.messagebox.showinfo('提示','修改成功！关闭本页面')
        except:
            tkinter.messagebox.showinfo("提示","修改失败")

    # 定义添加好友的函数
    def addfriends(self):
        self.friends_id = self.friends_entry.get()
        cursor.execute(f"SELECT * FROM USER_INFO WHERE QQ_NO='{self.friends_id}'")
        result = cursor.fetchone()
        if result:
            cursor.execute(f"INSERT INTO FRIEND (QQ_NO,FRIEND_QQ_NO) VALUES ('{self.id}','{self.friends_id}')")
            cursor.execute(f"INSERT INTO FRIEND (QQ_NO,FRIEND_QQ_NO) VALUES ('{self.friends_id}','{self.id}')")
            conn.commit()
            tkinter.messagebox.showinfo("提示","添加成功")
            # 更新将好友名字添加到列表框中
            self.friend_names_listbox.delete(0,tk.END)
            for name in self.get_friend_names():
                self.friend_names_listbox.insert(tk.END, name)
        else:
            tkinter.messagebox.showinfo("提示","没有这个人")
        return
        #print(self.friends_id)
    

    # 定义删除好友的函数
    def deletefriends(self):
        self.friends_id = self.friends_entry.get()
        cursor.execute(f"SELECT * FROM FRIEND WHERE FRIEND_QQ_NO='{self.friends_id}'")
        result = cursor.fetchone()
        if result:
            cursor.execute(f"DELETE FROM FRIEND WHERE FRIEND_QQ_NO='{self.friends_id}' AND QQ_NO ='{self.id}'")
            cursor.execute(f"DELETE FROM FRIEND WHERE FRIEND_QQ_NO='{self.id}' AND QQ_NO ='{self.friends_id}'")
            conn.commit()
            tkinter.messagebox.showinfo("提示","删除成功")
            # 更新将好友名字添加到列表框中
            self.friend_names_listbox.delete(0,tk.END)
            for name in self.get_friend_names():
                self.friend_names_listbox.insert(tk.END, name)
        else:
            tkinter.messagebox.showinfo("提示","没有这个人")
        return

    
    # 定义获取好友数量函数
    def get_friend_count(self):
        # 执行 SQL 查询
        cursor.execute("SELECT COUNT(*) FROM FRIEND WHERE QQ_NO = %s", (self.id))
        # 获取结果
        result = cursor.fetchone()
        # 返回结果
        return result[0]

    # 定义获取好友名字函数
    def get_friend_names(self):
        # 执行 SQL 查询
        cursor.execute("SELECT NICKNAME FROM USER_INFO WHERE QQ_NO = any(SELECT FRIEND_QQ_NO FROM FRIEND WHERE QQ_NO = %s)", (self.id))
        # 获取结果
        result = cursor.fetchall()
        # 返回结果
        return [row[0] for row in result]

    # 获取个人信息函数
    def get_info(self):
        # 执行 SQL 查询
        cursor.execute("SELECT * FROM USER_INFO WHERE QQ_NO = %s", (self.id))
        # 获取结果
        result = cursor.fetchone()
        # 返回结果
        client_sock.send(result[0].encode())
        return  result

    def goback(self,now,last):
        #隐藏当前窗口
        self.now_windows=now
        self.now_windows.withdraw()
        #显示上一个窗口
        self.last_windows=last
        self.last_windows.deiconify()
    
    def close_all(self):
        #销毁所有的窗口
        self.root.destroy()

    def on_select(self,event):
        # 获取选择的好友的索引
        index = self.friend_names_listbox.curselection()
        # 获取好友的名字
        """ name = self.friend_names_listbox.get(index)
        print(name) """
        # 输出选择的项的值
        for name in index:
        # 确保索引不超出列表的范围
            if name >= 0 and name < self.friend_names_listbox.size():
                #print(self.friend_names_listbox.get(name))
                # 打开聊天窗口
                self._sendmessage_windows(self.friend_names_listbox.get(name))
            else:
                pass

    #发送信息模块
    def sendmessage(self):
        self.myname = self.result[0]
        # 获取输入框中的消息
        message = self.message_entry.get()
        # 发送消息到客户端
        client_sock.send(message.encode())
        # 清空输入框
        self.message_entry.delete(0, tk.END)

        # 将消息添加到聊天记录中
        # 获取当前时间
        now = datetime.datetime.now()
        SEND_TIME = now.strftime("%Y-%m-%d %H:%M:%S")
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, f"{SEND_TIME}\n",'_self')
        self.chat_history.insert(tk.END, f"{self.myname}：{message}\n",'_self')
        self.chat_history.config(state=tk.DISABLED)
        # 对消息添加标签，实现右对齐
        self.chat_history.tag_config('_self',foreground='blue', justify='right')
        # 将消息记录到数据库中
        cursor.execute(
            "INSERT INTO MESSAGE_BOX (QQ_NO,FRIEND_QQ_NO,SEND_TIME ,MESSAGE) VALUES (%s,%s, %s,%s)",
            (self.myname,self.name,SEND_TIME, message)
        )
        conn.commit()

    # 聊天室窗口
    def _sendmessage_windows(self,name):
        self.name=name
        # 创建窗口
        self.sendmessage_windows = tk.Toplevel(self.root)
        self.sendmessage_windows.title('和'+str(self.name)+"的聊天窗口")

        # 创建聊天记录文本框
        self.chat_history = tk.Text(self.sendmessage_windows)
        self.chat_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 创建输入框和发送按钮
        self.message_frame = tk.Frame(self.sendmessage_windows)
        self.message_entry = tk.Entry(self.message_frame)
        self.send_button = tk.Button(self.message_frame, text="发送", command=self.sendmessage)

        # 布局
        self.message_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.message_entry.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.send_button.pack(side=tk.BOTTOM)

        self.ClientMessage()

    def ClientMessage(self):
        t=threading.Thread(target=self._get)
        t.setDaemon(True)
        t.start()
        self.sendmessage_windows.after(3,self.ClientMessage)

    def _get(self):
        recv_data = client_sock.recv(1024).decode('utf-8')
        if recv_data is not None:
            now = datetime.datetime.now()
            SEND_TIME = now.strftime("%Y-%m-%d %H:%M:%S")
            self.chat_history.config(state=tk.NORMAL)
            self.chat_history.insert(tk.END, f"{SEND_TIME}\n")
            self.chat_history.insert(tk.END, f"{self.name}：{recv_data}\n")
            self.chat_history.config(state=tk.DISABLED)


root=tk.Tk()
app=client(root)
root.mainloop()

# 关闭数据库连接
cursor.close()
conn.close()
