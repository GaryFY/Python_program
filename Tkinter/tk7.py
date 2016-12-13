# Radiobutton使用
from tkinter import *

root = Tk()

group = LabelFrame(root,text="最好的脚本语言是？",padx=5,pady=5)
group.pack(padx=10,pady=10)

LANGES = [
    ("Python",1),
    ("Perl",2),
    ("Ruby",3),
    ("Lua",4)]

v = IntVar()
v.set(1)

for lang,num in LANGES:
    #b = Radiobutton(group,text=lang,variable=v,value=num,indicatoron=False)
    b = Radiobutton(group,text=lang,variable=v,value=num)
    b.pack(anchor=W)

'''
Radiobutton(root,text="One",variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="Two",variable=v,value=2).pack(anchor=W)
Radiobutton(root,text="Three",variable=v,value=3).pack(anchor=W)
'''
mainloop()
