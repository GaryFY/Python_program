###面向对象程序设计的基本步骤###
#第一步：根据功能，抽象业务对象
#第二步：构建独立的业务模块，利用封装、继承、多态等抽象业务需求
#第三步：编写程序
#第四步：以对象为单位输入参数、开展测试

# 找到GPA最高的学生
# 定义Student类
class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
     
    def getName(self):
        return self.name
     
    def getHours(self):
        return self.hours
     
    def getQPoints(self):
        return self.qpoints
     
    def gpa(self):
        return self.qpoints/self.hours
     
def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)
     
def main():
    # 打开输入文件
    filename = input("Enter name the grade file: ")
    infile = open(filename, 'r')
    # 设置文件中第一个学生的记录为best
    best = makeStudent(infile.readline())
 
    # 处理文件剩余行数据
    for line in infile:
        # 将每一行数据转换为一个记录
        s = makeStudent(line)
        # 如果该学生是目前GPA最高的，则记录下来
        if s.gpa() > best.gpa():
            best = s
    infile.close()
 
    # 打印GPA成绩最高的学生信息
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())
 
if __name__ == '__main__':
    main()