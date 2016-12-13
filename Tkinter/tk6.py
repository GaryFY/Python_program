# Checkbutton使用
from tkinter import *

root = Tk()

GIRLS =["A","B","C","D"]

v = []

for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root,text=girl,variable=v[-1])
    b.pack(anchor=W)# 左对齐
    
'''
v = IntVar()

c = Checkbutton(root,text="测试一下",variable=v)
c.pack()

l = Label(root,textvariable=v)# 选中为1
l.pack()
'''
mainloop()
