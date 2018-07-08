# -*- coding: utf-8 -*-

"""
类/继承类
"""

from __future__ import print_function


class People:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.__score = s
        self.print_people()
        # self.__print_people() # 私有函数的作用

    def print_people(self):
        str = u'%s的年龄：%d, 成绩为：%.2f' % (self.name, self.age, self.__score)
        print(str)

    __print_people = print_people


class Student(People):
    def __init__(self, n, a, w):
        People.__init__(self, n, a, w)
        self.name = 'Student ' + self.name

    def print_people(self):
        str = u'%s的年龄：%d' % (self.name, self.age)
        print(str)


def func(p):
    p.age = 11


if __name__ == '__main__':
    p = People('Tom', 10, 3.14159) # 实例化类People时，会初始化People，同时调用了print_people(self):方法
    func(p) # p传入的是引用类型。对类People的参数self.age重新赋值
    p.print_people() # 调用print_people（）方法，此时已经对age参数重新赋值了

    # 注意分析下面语句的打印结果，是否觉得有些“怪异”
    j = Student('Jerry', 12, 2.71828) # 因为继承了people类，此时会先初始化变量，self.name， self.age，self.__score，self.print_people() （会调用student类的print_people方法）

    # 成员函数
    j.print_people() # 此时已经对self.name重新赋值
    People.print_people(j) # 此时已经对self.name重新赋值