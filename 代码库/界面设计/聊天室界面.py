'''
Author: ania0-art 75117340+ania0-art@users.noreply.github.com
Date: 2022-12-27 16:00:16
LastEditors: ania0-art 75117340+ania0-art@users.noreply.github.com
LastEditTime: 2022-12-30 14:57:26
FilePath: \程序设计\代码库\界面设计\聊天室界面.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import tkinter as tk
import pymysql
import datetime
# 连接到 MySQL 数据库
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="usechat",
    port=8888
)
cursor = conn.cursor()

# 定义发送消息函数
def send_message():
    # 获取输入框中的消息
    message = message_entry.get()

    # 清空输入框
    message_entry.delete(0, tk.END)

    # 将消息添加到聊天记录中
    # 获取当前时间
    now = datetime.datetime.now()
    SEND_TIME = now.strftime("%Y-%m-%d %H:%M:%S")
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END,f"{SEND_TIME}\n")
    chat_history.insert(tk.END, f"我：{message}\n")
    chat_history.config(state=tk.DISABLED)
    # 将消息记录到数据库中
    """ cursor.execute(
        "INSERT INTO MESSAGE_BOX (QQ_NO,FRIEND_QQ_NO,SEND_TIME ,MESSAGE) VALUES (%s,%s, %s,%s)",
        ('1','2',SEND_TIME, message)
    )
    conn.commit()
 """
# 创建窗口
root = tk.Tk()
root.title("聊天室")

# 创建聊天记录文本框
chat_history = tk.Text(root)
chat_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# 创建输入框和发送按钮
message_frame = tk.Frame(root)
message_entry = tk.Entry(message_frame)
send_button = tk.Button(message_frame, text="发送", command=send_message)

# 布局
message_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
message_entry.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
send_button.pack(side=tk.BOTTOM)

# 进入消息循环
root.mainloop()

# 关闭数据库连接
cursor.close()
conn.close()
