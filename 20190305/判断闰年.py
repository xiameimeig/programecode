'''4、用函数实现判断用户输入是否是闰年'''
def isyear(year):
    if year % 4 == 0 and year % 100 != 0:
        print('%s是闰年' % year)
    else:
        print('%s是平年' % year)


inyear = int(input('请输入需要判断的年份'))
isyear(year=inyear)
