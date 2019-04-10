# def counter(start=0):
#     def infuc():
#         nonlocal start
#         start += 1
#         print('此时内部函数调用的结果是',start)
#     return infuc
#
# my_func = counter(2)
# my_func()


def counter(start=0):
    a = [start]
    def infuc():

        sum = a[0] +1
        print('此时内部函数调用的结果是',sum)
    return infuc

my_func = counter(2)
my_func()