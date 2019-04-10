'''文件的基本操作'''
f = open("a.txt",encoding='utf-8')
# f = open("a.txt")
print(f.encoding)
# ret2 = open("b.txt",'w')
# ret3 = open("c.txt",'r')


ret = f.read(200)
print(ret)
f.readli5ne()
f.readlines()
# 关闭文件
f.close()