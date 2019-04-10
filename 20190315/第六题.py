import random

ret = random.randint(1,2)
"""Return random integer in range [a, b], including both end points."""
print(ret)

'''
6、要求： 可以指定一批生成的个数，可以指定数值的范围，可以调整每批生成数字的个数。

'''


class RandomNumber(object):
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count

    def numbers(self):
        return [random.randint(self.start,self.end) for _ in range(self.count)]


if __name__ == '__main__':
    a = RandomNumber(2,9,5)
    ret = a.numbers()
    print(ret)