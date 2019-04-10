'''
1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
2、创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。重写__str__方法，返回student的信息。
3、创建Teacher类，继承Person类，属性有学院college，专业professional，重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序’
4、创建三个学生对象，分别打印其详细信息
5、创建一个老师对象，打印其详细信息
6、学生对象调用study方法
7、将三个学员添加至列表中，通过循环将列表中的对象打印出来，print(Student对象)。

'''

class Person(object):
    '''创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息'''
    def __init__(self,name,age,gender):

        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        # print('姓名：%s,年龄：%s，性别：%s'%(self.name,self.age,self.gender))
        print('姓名：',self.name,'年龄',self.age,'性别',self.gender)



class Student(Person):
    '''
    创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teachobj方法返回的信息。重写__str__方法，返回student的信息。
    '''
    def __init__(self,name,age,gender,college,classes):
        super(Student, self).__init__(name,age,gender)
        self.college = college
        self.classes = classes

    def personInfo(self):
        super(Student, self).personInfo()
        print('学校：%s，班级：%s' % (self.college, self.classes))

    def study(self,teacher):
        '''创建方法study参数为Teacher对象'''
        target = teacher.teachobj()
        print('老师,%s,我终于学会了！'%target)
    def __str__(self):
        return '姓名：%s,年龄：%s，性别：%s，学校：%s，班级：%s' % (self.name, self.age, self.gender,self.college,self.classes)


class Teacher(Person):

    def __init__(self,name,age,gender,college,professional):
        super(Teacher, self).__init__(name,age,gender)
        self.college = college
        self.professional = professional

    def personInfo(self):
        super(Teacher, self).personInfo()
        print('学校：%s，专业：%s' % (self.college, self.professional))

    def teachobj(self):
        '''创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序,返回知识点'''
        return '今天讲了如何用面向对象设计程序'


if __name__ == '__main__':
    zhang = Student('张三',18,'boy','北大','计算机科学与技术')
    zhang.personInfo()

    teacher = Teacher('张二毛',50,'male','理工','植物种植')
    zhang.study(teacher)
    teacher.personInfo()