from tkinter import *
from tkinter.filedialog import askopenfilename

import md5

frameT = Tk()
frameT.geometry('500x200+400+200')
frameT.title('数字签名')
frame = Frame(frameT)
frame.pack(padx=10, pady=10)  # 设置外边距
frame_1 = Frame(frameT)
frame_1.pack(padx=10, pady=10)  # 设置外边距
v1 = StringVar()
v2 = StringVar()
ent = Entry(frame, width=50, textvariable=v1).pack(fill=X, side=LEFT)  # x方向填充,靠左
ent = Entry(frame_1, width=50, textvariable=v2).pack(fill=X, side=LEFT)  # x方向填充,靠左

def fileopen():
    file_sql = askopenfilename()
    if file_sql:
        v1.set(file_sql)

def md5hash():
    filepath=v1.get()
    md5hash= md5.get_md5_01(filepath)
    v2.set(md5hash)
    pass

btn1 = Button(frame, width=20, text='选择文件', font=("宋体", 14), command=fileopen).pack(fil=X, padx=10)
btu2 = Button(frame_1, width=20, text='数据摘要', font=("宋体", 14), command=md5hash).pack(fill=X, padx=10)
frameT.mainloop()
