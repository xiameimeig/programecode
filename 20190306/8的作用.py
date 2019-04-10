'''*的作用'''
def info(name,age,gender):
    print(name,age,gender)


a = ['zhang1',19,'boy']
b = ['zhang2',1,'boy']
c = ['zhang3',9,'boy']

info(a[0],a[1],a[2])
info(*b)