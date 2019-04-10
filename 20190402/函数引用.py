'''闭包的基础问题，引用'''
def old():
    print('被引用的基础函数')

old()

# # 函数引用
new = old
#
print(id(old))
print(id(new))
#
print('###########使用引用函数############')
new()