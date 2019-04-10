# 第一步，将TXT文件里面的内容读取出来，并且赋值给全局变量
info_list = []
def openfile():
    '''
    这个函数实现从TXT文件里面读取内容，并且读取出来的信息列表，并抛出
    :return:
    '''
    file = open('info.txt')
    file_list = eval(file.read())
    file.close()
    return file_list

def savefile(data):
    '''
    这个函数实现了全局变量Info——list 的保存，放入到TXT文件里面
    data:指的是全局变量Info_list
    :return:
    '''
    file = open('info.txt','w+')
    file.write(str(data))
    file.close()


def add_card():
    # 实现增加名片的功能
    global info_list
    # todo 与用户交互，让用户输入具体的信息
    inname = input('请输入需要存储的名字:')
    intel = input('请输入联系方式:')
    incompany = input('请输入公司名称:')
    induty = input('请输入公司职位:')
    # 判断用户是否存在，如果存在，就打断程序，如果不存在，存储信息
    for obj in info_list:
        if obj['tel'] == intel:
            print('用户已经存在')
            return
    person_dict = {}
    person_dict['name'] = inname
    person_dict['tel'] = intel
    person_dict['company'] = incompany
    person_dict['duty'] = induty
    # todo 将每一个新增的字典插入到原始的列表中去
    info_list.append(person_dict)
    # todo:保存到txt
    savefile(info_list)


def main():
    file_list = openfile()
    global info_list
    info_list = file_list
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
        # 根据用户的输入，指定不同的操作
        if choice == '1':
            add_card()
        # elif choice == '2':
        #     del_card()
        # elif choice == '3':
        #     change_card()
        # elif choice == '4':
        #     search_info()
        # elif choice == '5':
        #     quit = input('确认退出请按q:')
        #     if quit == 'q':
        #         break
        else:
            print('请输入正确的指令')


if __name__ == '__main__':
    main()