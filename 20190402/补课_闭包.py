'''


def 外部函数（参数）：
    def 内部函数（参数） ：
        使用外部函数的参数（环境变量）
    Return 内部函数的引用（就是我们的函数名，不需要加括号）
'''

def wrapp():
    def inner():
        print('闭包函数')
    return inner

func = wrapp()
func()