try:
    f = open('a.txt')
    try:
        ret=f.readline()
        print(ret)
    finally:
        f.close()
        print('文件已经关闭')
except FileNotFoundError:
    print('文件未找到')

except UnicodeDecodeError:
    print('编码错误')

except Exception as e:
    print(e)


