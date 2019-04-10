class Cat(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if  not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            return cls.__instance
        return cls.__instance

    def __init__(self):
        print('此时调用这个init')



if __name__ == '__main__':
    cat = Cat()
    cat.name = 'tom'
    print(cat.name)

    cat2 = Cat()
    cat2.name = None
    # print(cat2.name)
    print(cat.name)