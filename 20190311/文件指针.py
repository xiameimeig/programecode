# '''实现文件指针'''
# f = open('../20190308/a.txt')
# ret = f.read(7)
# ret1 = f.tell()
#
# print('读取的内容：',ret)
# print('指针的位置：',ret1)
# f.close()

# f = open('b.txt','r+')
# ret = f.tell()
# print('当前指针的位置:',ret)
# f.read(3)
# ret1 = f.tell()
# print('当前指针的位置:',ret1)
# f.seek(0,2)
# f.writelines()
# #定位到文件的末尾0-代表开头位置1代表当前位置2代表末尾
# ret2 = f.tell()
# print('当前指针的位置:',ret2)


f = open('c.txt','w+')
new_list = ['hello world\n','hello python\n']
f.writelines(new_list)
f.writelines('new_list')
f.close()