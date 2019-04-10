old_file = open('a.txt','r',encoding='utf-8')
new_file = open('b.txt','a+',encoding='utf-8')

for obj in old_file.readlines():
    new_file.write(obj)