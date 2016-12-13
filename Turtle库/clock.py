#模拟时钟，要求时钟根据计算机系统时间实时动态更新

from turtle import *
from datetime import *
#画的时候需要有停顿，像素的跨越操作
def Skip(step):
    penup()
    forward(step)
    pendown()
#定义表针
def mkHand(name, length):
    #注册Turtle形状，建立表针Turtle
    reset()
    Skip(-length*0.1)#定义几何中心
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm)#注册Turtle形状命令
 
def Init():
	#建立Turtle对象并初始化
    global secHand, minHand, hurHand, printer
    mode("logo")#重置Turtle指向北
    #建立三个表针Turtle并初始化
    mkHand("secHand", 125)
    mkHand("minHand",  130)
    mkHand("hurHand", 90)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    #建立输出文字Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()
     
def SetupClock(radius):
    #建立表的外框
    reset()
    pensize(7)#画笔大小
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:#每5个间隔一个小线段
            forward(20)
            Skip(-radius-20)
        else:#其余为小圆点
            dot(5)
            Skip(-radius)
        right(6)
         
def Week(t):    
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]
 
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)
 
def Tick():
    #绘制表针的动态显示
    t = datetime.today()#获得当前时间
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)#角度
     
    tracer(False)  
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()#归位到原点
    tracer(True)
 
    ontimer(Tick, 100)#100ms后继续调用tick
 
def main():
    tracer(False)#动画关闭
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()
 
if __name__ == "__main__":       
    main()