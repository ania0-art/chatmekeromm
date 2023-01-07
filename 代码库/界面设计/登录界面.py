'''
Author: ania0-art 75117340+ania0-art@users.noreply.github.com
Date: 2022-12-27 15:02:58
LastEditors: ania0-art 75117340+ania0-art@users.noreply.github.com
LastEditTime: 2022-12-27 21:07:41
FilePath: \程序设计\代码库\界面设计\登录界面.py
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

# 定义登录函数
def login():
    # 获取用户名和密码
    username = username_entry.get()
    password = password_entry.get()

    # 执行 SQL 查询，检查用户名和密码是否正确
    cursor.execute(f"SELECT * FROM USER_LOGIN WHERE QQ_NO='{username}' AND PASSWORD='{password}'")
    result = cursor.fetchone()
    if result:
        # 如果用户名和密码正确，显示登录成功信息
        label.config(text="登录成功！")
    else:
        # 如果用户名或密码错误，显示错误信息
        label.config(text="用户名或密码错误，请重试！")

# 定义注册函数
def register():
    # 跳转到注册界面
    pass

# 创建窗口
root = tk.Tk()
root.title("用户登录")
root.geometry("500x250")

# 创建用户名输入框和密码输入框
username_label = tk.Label(root, text="用户名：")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="密码：")
password_entry = tk.Entry(root, show="*")

# 创建登录按钮和注册按钮
login_button = tk.Button(root, text="登录", command=login)
register_button = tk.Button(root, text="注册", command=register)

# 创建提示信息标签
label = tk.Label(root)

# 布局
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()
register_button.pack()
label.pack()

#进入消息循环
root.mainloop()

#关闭数据库连接
cursor.close()
conn.close()