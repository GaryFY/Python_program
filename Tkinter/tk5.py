from tkinter import *

# 当按下按钮后，调用函数
def callback():
    var.set("this is Jordan")
    
root = Tk()

# 定义两个frame
frame1 = Frame(root)
frame2 = Frame(root)

# 定义变量用于后面对字符串的调用
var = StringVar()
var.set("下载内容有问题！")

textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT,
                  )
textLabel.pack(side = LEFT)

photo = PhotoImage(file="18.gif")
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side = RIGHT)

theButton = Button(frame2,text="我已满18",command=callback)
theButton.pack()

# 留出10空间
frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()
