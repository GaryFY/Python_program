from tkinter import *

root = Tk()

#textLabel = Label(root,text="下载内容有问题！")
#textLabel.pack(side = LEFT)

photo = PhotoImage(file="18.gif")
theLabel = Label(root,
                 text="学python",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=("楷体",20),
                 fg="white"
                 )
theLabel.pack()

mainloop()
