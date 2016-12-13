# copy document
# 遍历文件简化框架
# file = open(someFile,"r")
# For line in file:
# 	#处理一行文件内容
# file.close()
def main():
	# 用户输入文件名
	f1 = input("Enter a souce file:").strip()
	f2 = input("Enter a souce file:").strip()
	
	# 打开文件
	infile =  open(f1,"r")
	outfile = open(f2,"w")
	
	# 拷贝数据
	countLines = countChars = 0
	for line in infile:
		countLines += 1 
		countChars += len(line)
		outfile.write(line)
	print(countLines,"lines and",countChars,"chars copied")
	
	infile.close()
	outfile.close()
	
main()
		