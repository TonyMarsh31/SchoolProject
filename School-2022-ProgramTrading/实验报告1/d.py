# 使用文件函数进行文件读写操作

# 通过open函数打开文件
file = open('./sh000001.csv')
# 读取数据
for line in file.readlines():
    print(line)
# 关闭文件
file.close()