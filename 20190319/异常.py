try:
    # print(a)
    print('这次我没有发生错误')
except (IOError,NameError):
    #捕获指定的错误类型
    print('##########except################')
else:
    print('$$$$$$$$$$进入else$$$$$$$$$$$')

finally:
    print('**********进入finally**************')