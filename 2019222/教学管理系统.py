'''实现一个教学管理系统，动态的实现访客的信息展示，要求展示用户名和专业，登录的时候使用用户名和密码'''
# 原始数据库密码，模拟数据库取出的数据
password = '123456'
username = 'admin'
subject = 'python'

# 键盘中获取访客用户名和密码
inusername = input('请输入您的用户名：')
inpassword = input('请输入您的密码：')


if (inusername == username) and (inpassword==password):
    '''实现用户正确登录，展示页面'''
    print('*********************教学管理系统********************')
    print('您的用户名：%s'%inusername)
    # print(inusername)
    print('您的专业：%s'%subject)
    # print(subject)
    print('*****************************************************')
else:
    '''用户用户名或者密码错误，展示'''

    print('*********************教学管理系统********************')
    print('用户名或者密码错误')
    print('*****************************************************')