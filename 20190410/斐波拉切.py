class F:
    def __init__(self,month):
        '''
        初始化操作，需要传入控制的次数
        :param month: 控制生成对应的数据
        '''
        self.month = month
        self.a = 0
        self.b = 1
        self.current_index = 0 # 当前迭代的次数的索引
        pass
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.month:
            result = self.a
            self.a,self.b = self.b,self.a+self.b
            self.current_index += 1
            return result
        else:
            raise StopIteration



if __name__ == '__main__':
    f = F(10)
    for i in f:
        print(i)