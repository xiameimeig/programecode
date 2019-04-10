class MyException(Exception):
    '''这是我们自定义的异常'''
    def __init__(self):
        super().__init__()
        self.errormsg = '这是一个错误信息'
    def __str__(self):
        return self.errormsg


if __name__ == '__main__':

    try:
        s = input('请你输入一个值')
        if len(s) < 3:
            raise MyException()

    except MyException as e:
        print('进入except')
        print(e)

    else:
        print('此时没有任何错误')
    finally:
        print('必须要走的')