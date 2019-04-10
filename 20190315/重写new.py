class Cat(object):
    def __new__(cls):
        obj = super().__new__(cls)
        obj.name = 'haha'
        return obj



if __name__ == '__main__':
    a = Cat()
    print(a.name)