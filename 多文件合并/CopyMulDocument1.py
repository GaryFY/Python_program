#利用字典将两个通讯录文本合并为一个文本


def main():
        ftele2=open('TeleAddressBook.txt','rb')
        ftele1=open('EmailAddressBook.txt','rb')
 
        ftele1.readline()#跳过第一行
        ftele2.readline()
        lines1 = ftele1.readlines()
        lines2 = ftele2.readlines()
 
        dic1 = {}   #字典方式保存
        dic2 = {}
 
 
        for line in lines1:#获取第一个本文中的姓名和电话信息
                elements = line.split()
                #将文本读出来的bytes转换为str类型
                dic1[elements[0]] = str(elements[1].decode('gbk'))
                 
        for line in lines2:#获取第二个本文中的姓名和电话信息
                elements = line.split()
                dic2[elements[0]] = str(elements[1].decode('gbk'))
 
        ###开始处理###
		#生成数据表头
        lines = []
        lines.append('姓名\t    电话   \t  邮箱\n')
 
        for key in dic1:
            s= ''
            if key in dic2.keys():#处理与表2重名的信息
                    s = '\t'.join([str(key.decode('gbk')), dic1[key], dic2[key]])
                    s += '\n'
            else:#处理其他信息
                    s = '\t'.join([str(key.decode('gbk')), dic1[key], str('   -----   ')])
                    s += '\n'
            lines.append(s)
             
        for key in dic2:#处理列表2中剩余的姓名
            s= ''
            if key not in dic1.keys():
                    s = '\t'.join([str(key.decode('gbk')), str('   -----   '), dic2[key]])
                    s += '\n'       
            lines.append(s)
		#将新生成的合并数据写入新文件
        ftele3 = open('AddressBook.txt', 'w')
        ftele3.writelines(lines)
		#关闭文件
        ftele3.close()
        ftele1.close()
        ftele2.close()
        print("The addressBooks are merged!")
 
if __name__ == "__main__":
        main()