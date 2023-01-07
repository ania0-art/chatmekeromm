'''
Author: ania0-art 75117340+ania0-art@users.noreply.github.com
Date: 2022-12-27 15:15:58
LastEditors: ania0-art 75117340+ania0-art@users.noreply.github.com
LastEditTime: 2022-12-27 21:23:17
FilePath: \程序设计\代码库\界面设计\注册界面.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pymysql
import tkinter as tk

# 连接到 MySQL 数据库
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="usechat",
    port=8888
)
cursor = conn.cursor()

# 定义注册函数
def register():
    # 获取用户名、密码、确认密码
    username = username_entry.get()
    password = password_entry.get()
    password_confirm = password_confirm_entry.get()

    # 判断密码是否一致
    if password != password_confirm:
        label.config(text="两次输入的密码不一致！")
        return

    # 判断用户名是否已存在
    cursor.execute(f"SELECT * FROM USER_LOGIN WHERE QQ_NO='{username}'")
    result = cursor.fetchone()
    if result:
        label.config(text="用户名已存在！")
        return

    # 插入新用户
    cursor.execute(f"INSERT INTO USER_LOGIN (QQ_NO, password) VALUES ('{username}', '{password}')")
    conn.commit()

    # 注册成功，显示提示信息
    label.config(text="注册成功！")

# 创建窗口
root = tk.Tk()
root.title("用户注册")
root.geometry("500x250")
# 创建用户名输入框、密码输入框、确认密码输入框
entry_var = tk.StringVar()
username_label = tk.Label(root, text="用户名：")
username_entry = tk.Entry(root,textvariable=entry_var)
entry_var.set("请输入八位数")
password_label = tk.Label(root, text="密码：")
password_entry = tk.Entry(root, show="*")
password_confirm_label = tk.Label(root, text="确认密码：")
password_confirm_entry = tk.Entry(root, show="*")

# 创建注册按钮
register_button = tk.Button(root, text="注册", command=register)

# 创建提示信息标签
label = tk.Label(root)
#布局
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
password_confirm_label.pack()
password_confirm_entry.pack()
register_button.pack()
label.pack()

#进入消息循环
root.mainloop()

#关闭数据库连接
cursor.close()
conn.close()