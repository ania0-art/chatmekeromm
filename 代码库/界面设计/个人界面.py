'''
Author: ania0-art 75117340+ania0-art@users.noreply.github.com
Date: 2022-12-27 16:20:18
LastEditors: ania0-art 75117340+ania0-art@users.noreply.github.com
LastEditTime: 2022-12-27 21:08:59
FilePath: \程序设计\代码库\界面设计\个人界面.py
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

# 定义获取好友数量函数
def get_friend_count():
    # 执行 SQL 查询
    cursor.execute("SELECT COUNT(*) FROM FRIEND WHERE QQ_NO = %s", (user_id,))
    # 获取结果
    result = cursor.fetchone()
    # 返回结果
    return result[0]

# 定义获取好友名字函数
def get_friend_names():
    # 执行 SQL 查询
    cursor.execute("SELECT FRIEND_QQ_NO FROM FRIEND WHERE QQ_NO = %s", (user_id,))
    # 获取结果
    result = cursor.fetchall()
    # 返回结果
    return [row[0] for row in result]

# 创建窗口
root = tk.Tk()
root.title("个人界面")
root.geometry("500x250")
# 获取当前用户的 ID
user_id = 1

# 显示好友数量
friend_count_label = tk.Label(root, text=f"好友数量：{get_friend_count()}")
friend_count_label.pack()

# 创建列表框
friend_names_listbox = tk.Listbox(root)

# 将好友名字添加到列表框中
for name in get_friend_names():
    friend_names_listbox.insert(tk.END, name)

# 显示列表框
friend_names_listbox.pack()

# 运行窗口
root.mainloop()
