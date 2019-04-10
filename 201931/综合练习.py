'''

需要完成的基本功能：
1.添加名片
2.删除名片
3.修改名片
4.查询名片
5.退出系统
程序运行后，除非选择退出系统，否则重复执行功能
'''

# info_list = [{'name':'wang','age':18,'company':'ali'},['xiaowang',10,'huawei']]
info_list = []
# 所有的名片存放在这个列表里面
while True:
    # 显示出所有的选择
    print('****************名片管理系统*********************')
    print('1.添加名片')
    print('2.删除名片')
    print('3.修改名片')
    print('4.查询名片')
    print('5.退出系统')
    print('*************************************************')
    #与用户交互，让他输入选择
    choice = input('请输入您的选择') #input输入的内容是字符串的类型
    #根据用户的输入，指定不同的操作
    if choice == '1':
        # 实现增加名片的功能
        # todo 与用户交互，让用户输入具体的信息
        inname = input('请输入需要存储的名字:')
        intel = input('请输入联系方式:')
        incompany = input('请输入公司名称:')
        induty = input('请输入公司职位:')
        # 设置一个标志，表示是否存在重复用户，1代表有重复数据 2代表没有重复数据
        flag = 0 # 初始状态表示没有重复数据
        # TODO 判断用户是否已经存在
        for obj in info_list: #表示遍历列表，拿出每一条的名片数据

            if obj['tel'] == intel: #判断字典中是否存在用户输入的号码，即真正判断是否有重复数据
                print('已经存在')
                flag = 1

                # 填写一个语句，打断程序，不让继续执行添加操作
        # 根据flag的值，来判断是否需要将新的字典插入列表
        if flag == 0:
            '''这是没有重复数据进入的操作'''
        # TODO 增加一个新字典，用来存储一个新名片
            person_dict = {}
            person_dict['name'] = inname
            person_dict['tel'] = intel
            person_dict['company'] = incompany
            person_dict['duty'] = induty
            # todo 将每一个新增的字典插入到原始的列表中去
            info_list.append(person_dict)
            print(info_list)
        else:
            print('重复数据，跳出循环')

    elif choice == '2':
        # 提示用户输入需要删除的电话号码
        intel = input('请输入需要删除的电话号码')
        # 判断是否存在这条数据
        for obj in info_list:
            print(obj)
            if obj['tel'] == intel:
                print('找到数据并删除')
                # 让用户确实是否删除
                inq = input('如果确认删除请输入q:')
                if inq == 'q':
                    info_list.remove(obj)
                else:
                    print('放弃修改')
        print(info_list)
        pass
    elif choice == '3':
        print('3.修改名片')
    elif choice == '4':
        print('4.查询名片')
    elif choice == '5':
        quit = input('确认退出请按q:')
        if quit == 'q':
            break
    else:
        print('请输入正确的指令')




