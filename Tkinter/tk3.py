from tkinter import *

root = Tk()

textLabel = Label(root,text="下载内容有问题！")
textLabel.pack(side = LEFT)

photo = PhotoImage(file="18.gif")
imgLabel = Label(root,image=photo)
imgLabel.pack(side = RIGHT)

mainloop()
