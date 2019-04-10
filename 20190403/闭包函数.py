def warpper():
    print('begin warpper')
    def inner():
        print('inner')
    print('end warpprt')
    return inner


if __name__ == '__main__':
    func = warpper() # func=inner
    func() # func() == inner()