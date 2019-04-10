'''复制凉凉并改名'''
# 打开旧文件
old_file = open('liangliang.mp3','rb')
# 打开新文件
new_file = open('凉凉.mp3','wb')

# 读取旧文件里面所有的内容，以列表的形式返回
list_obj = old_file.readlines()
print(list_obj)

# 将读取的旧文件里面的内容，写入到新文件，
# 因为readlines是按照列表的形式返回，
# 所以采用遍历列表的形式，按行写入
for obj in list_obj:
    new_file.write(obj)

# 关闭文件
old_file.close()
new_file.close()