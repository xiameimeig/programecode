class Myerro(Exception):
    def __str__(self):
        self.error='这是错误'
        return self.error
try:
    raw_input=input('请输入字符串:')
    if len(raw_input)<5:
        raise Myerro
except Myerro as a:
    print('The input is of length %s,expecting at least 5'%len(raw_input))
    print(a)
else:
    print('print success')
finally:
    print('这是必须要经历的过程')