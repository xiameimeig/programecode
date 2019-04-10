def person_info(**kwargs):
    '''

    :param kwargs: 将所有的关键字参数打包成字典
    :return:
    '''
    print(kwargs)

person_info(name='xiaowang',age=18)
person_info(age=18)