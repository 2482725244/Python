from functools import reduce

# rand = random.randint(1, 10)
# print(rand)
# num = int(input('请输入你要猜的数字\n'))
# if num == rand:
#     print("Your input is correct!")
# else:
#     print("You input is fail!")

# 输入一个整数百位和十位大于十吗

# number = input('请输入一个随机的四位数\n')
# number = int(number)
# if (number // 10 % 10) + (number // 100 % 10) > 10:
#     print("success!")
# else:
#     print("fail!")

# 3.随机产生两个随机数1-10，判断和是否大于8并且差小于等于3
# num1 = random.randint(1,10)
# num2 = random.randint(1,10)
#
# print("num1 = %d, num2 = %d" %(num1, num2))
#
# if num1 + num2 > 8 and abs(num1 - num2) <= 3:
#     print('success!')
# else:
#     print('fail!')

# 4.年终奖的发放
'''
1-5: 1000元
5-10：10000元
10-100：奔驰
100以上：大牛
低于1：玩偶
'''
# num = input('请输入你的业绩\n')
# num = float(num)
# num = int(num)
# if 1 <= num < 5:
#     print("奖励1000元")
# elif 5 <= num < 10:
#     print("奖励10000元")
# elif 10 <= num < 100:
#     print("奖励奔驰")
# elif num >= 100:
#     print("奖励大牛")
# else:
#     print("奖励一个玩偶")

# 5.人员管理系统
# print("欢迎进入银行人员管理系统",end = '')
# choice = input('''
# 请选择你的操作
# 1.查找员工
# 2.添加员工
# 3.修改员工
# 4.删除员工
# 0.退出系统
# ''')
# choice = int(choice)
# if choice == 1:
#     print("您已成功进入查找模式")
# elif choice == 2:
#     print("您已成功进入添加模式")
# elif choice == 3:
#     print("您已成功进入修改模式")
# elif choice == 4:
#     print("您已成功进入删除模式")
# elif choice == 0:
#     print("您已成功退出系统")

# while循环

# n = 1
# while n <= 10:
#     print(n)
#     if n == 15:
#         break
#     n += 1
# else:
#     print("success!")

# for循环

# for i in range(1,10,5):
#     print(i)
#     if i == 6:
#         break
# else:
#     print("success!")

# 列表
# mystr = ['tom','lisa','as']
# mystr.append('cctv')
# print(mystr)
# mystr.pop()
# print(mystr)
# mystr[0] = 'asd'
# print(mystr)
# mystr.reverse()
# print(mystr)
#
# print(mystr.index('lisa'))

# 列表循环
# arr = ['tom', 'list', 'cctv1']
# i = 0
# while i < len(arr):
#     print(arr[i])
#     i += 1
#
# for p in arr:
#     print(p)

# 元组
# tuple = (10,29,33,55)
# # tuple[0] = 11
# print(len(tuple))
# print(tuple.index(29))
# print(tuple)
# print(type(tuple))
# for t in tuple:
#     print(t)

# 字典
# my_dict = {"name": "binbin","age": 18,"sex": "男"}
#
# print(my_dict["name"])
# print(my_dict.get("age"))
# print(my_dict)
# my_dict["id"] = "1312"
# print(my_dict)
# my_dict["name"] = "bb"
# print(my_dict)
# #my_dict.clear()
# print(my_dict)
# my_dict2 = {}
# print(type(my_dict2))
# my_dict3 = dict()
# print(type(my_dict3))
# my_dict.pop("name")
# print(my_dict)
# my_dict.pop("age")
# print(my_dict)
#
# print(my_dict.keys())
# print(my_dict.values())
#
# print(my_dict.items())
#
# for item in my_dict.items():
#     print(item)


# 集合
# my_set1 = {10,20,30,40,50,20,10}
# my_set2 = set()
# print(type(my_set1))
# print(my_set1)
#
# my_set3 = {10}
# print(type(my_set3))
# my_set3.add(20)
# my_set3.add(10)
# print(my_set3)
# my_set3.update([20,30,40,50])
# print(my_set3)
# num = my_set3.pop()
# print(num)
# print(my_set3)
# # del my_set3
# # del(my_set3)
# print("del")
# print(my_set3)
# for i in my_set3:
#     print(i)

# 运算符
# str1 = "abc"
# str2 = "bcd"
# print(str2+str1)
#
# str3 = 'a'
# print(str1 * 10)
#
# tuple1 = (1,2,3)
# tuple2 = (3,4,5)
#
# print(tuple2+tuple1)
# print(tuple2 * 3)
#
# arr  = [1,2,3]
# print(type(arr))
# print(arr * 10)
#
# print(2 in arr)
# print(20 in arr)
# print(2 not in arr)

# 列表推导式

# list = list()
#
# list = [i for i in range(1,10,2)]
# print(list)
# list2 = [i for i in range(10) if i % 2 == 0]
# print(list2)
# list3 = [i+j for i in range(3) for j in range(3)]
# print(list3)

# list4 = [ (i,j) for i in range(3) for j in range(3)]
# print(list4)

# dict1 = {i:j for i in range(3) for j in range(3)}
# print(dict1)

# list1 = ["name","age","sex"]
# list2 = ["lisa","18","woman"]
#
# dict2 = {list1[i]:list2[i] for i in range(3)}
# print(dict2)
# list4 = [1,1,2,3,4]
# set1 = {i*i for i in list4}
# print(set1)
#
# tuple9 = (i*i for i in list4)
# print(tuple9)
# list1 = [1,1,2,3]
# tuple1 = (1,2,3)
# set1 = {1,2,3}
# print(list(set1))
# print(set1)
# print("aaa",set(list1))
# 函数
# def print_func():
#     print("hello world")
#     return 3
# num = print_func()
# print(num)
#
# def sum(a,b,c):
#     h = a + b
#     s = print_func() + c
#     if h+s > 10:
#         print(h+s)
#         return 1
#     else:
#         return -1
#
# print(sum(6,7,8))

# 学生管理系统
# studens = list()
# count_id = 1
#
# def menu_print():
#     print("欢迎进入学生管理系统")
#     print("1.添加学生")
#     print("2.删除学生")
#     print("3.查询学生")
#     print("4.修改学生")
#     print("5.展示所有学生")
#     print("6.退出系统")
#
# def add_func(info):
#     global studens
#     studens.append(student)
#
# def delete_func(id):
#     global studens
#     for i in range(len(studens)):
#         if studens[i]['id'] == id:
#             #del studens[i]
#             studens.pop(i)
#
# def find_by_id_func(id):
#     global studens
#     for i in range(len(studens)):
#         if studens[i]['id'] == id:
#             print(studens[i])
#
# def update_func(id):
#     global studens
#     for i in range(len(studens)):
#         if studens[i]['id'] == id:
#             print(studens[i])
#
# menu_print()
# while True:
#     choose = int(input("请确认你的选择\n"))
#     if choose == 1:
#         name = input("请输入你的名字")
#         age = input("请输入你的年龄")
#         sex = input("请输入你的性别")
#         student = {"id": count_id, "name": name, "age": age, "sex": sex}
#         count_id += 1
#         add_func(student)
#         print("添加成功")
#     elif choose == 2:
#         id = input("输入你想操作的id:")
#         delete_func(int(id))
#         print("删除成功")
#     elif choose == 3:
#         id = input("输入你想操作的id:")
#         find_by_id_func(int(id))
#         print("查询成功")
#     elif choose == 4:
#         id = input("输入你想操作的id:")
#
#         update_func(int(id))
#         print("修改成功")
#     elif choose == 5:
#         print(studens)
#         print("展示成功")
#     elif choose == 6:
#         print("退出成功")
#         break
#     else:
#         print("输入错误，请重新输入")

# lambda
# fn1 = lambda: 100
# print(fn1())
#
# fn2 = lambda a: a * a
# print(fn2(6))
#
# fn3 = lambda a, b: a + b
# print(fn3(3, 4))
#
# fn4 = lambda a, b, c=100: a + b + c
# print(fn4(1, 2))
# print(fn4(1, 2, 400))
# print(fn4(a=1, b=2, c=300))
#
# fn5 = lambda *args: args
# print(fn5(1, 2, 3))
#
# fn6 = lambda **kwargs: kwargs
# print(fn6(name = "lisa", age = 18))
#
# fn7 = lambda a, b: a if a > b else b
# print(fn7(8,7))

# 文件
# file = open("test.txt","r")
# print(file.name)
# print(file.readline())
# print(file)
# file.close()

# # 字典排序
# students = [{"age":13,"name":"lisa",},{"age":20,"name":"aaa",},{"age":11,"name":"son",}]
# print(students)
# students.sort(key=lambda x: x["name"])
# print(students)
# students.sort(key=lambda x: x["age"])
# print(students)

# 高阶函数

# def func(a,b,f):
#     return f(a) + f(b)
#
# print(func(3,-6,abs))
# print(func(1.2,1.9,round))
#
# def add(a,b):
#     return a+b
#
# def func2(a,b,f):
#     return f(a,b)
#
# print(func2(13,23,lambda a,b: a+b))
# arr = [1,2,3,4,5]
# def su(a):
#     return a**2
# new_arr = map(su,arr)
# print(new_arr)
# print(list(new_arr))
# new_arr2 = map(lambda x: x**3,arr)
# print(list(new_arr2))
# print(arr)
#
# def func3(x):
#     if x % 2 == 0:
#         return x
#
#
# new_arr3 = filter(func3,arr)
# print(list(new_arr3))
#
# result = reduce(lambda a,b: a+b,arr)
# print(result)

# 文件操作
# file = open("test.txt",'a+',encoding="utf-8")
# print("open success")
# file.seek(0)
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# 文件备份
# old_name = input("请输入需要备份的文件名称\n")
# try:
#     file_r = open(old_name,'rb')
# except FileNotFoundError:
#      print("没有该文件")
#      exit(1)
# else:
#      print("验证成功")
#
# index = old_name.rindex('.')
# new_name2 = old_name[:index] + "[副本]" + old_name[index:]
# new_name = "python_" + old_name
# file_w = open(new_name2,'wb')
# while True:
#     content = file_r.read(1024)
#     if len(content) == 0:
#         break
#     file_w.write(content)
# print("复制完成")
# file_r.close
# file_w.close

# import os
# print(os.getcwd())
# try:
#     os.mkdir('aaa')
# except:
#     print("已创建")
# os.rmdir('aaa')
# os.chdir("aaa")
# print(os.getcwd())
# os.rename('aaa','bbb')
# print(os.listdir())
# 练习
# flag = 2
# if flag == 1:
#     os.chdir('aaa')
#     list_dir = os.listdir()
#     print(list_dir)
#
#     for i in list_dir:
#         new_name = "python_" + i
#         os.rename(i,new_name)
# if flag == 2:
#     os.chdir('aaa')
#     list_dir = os.listdir()
#     for i in list_dir:
#         new_name = i[7:]
#         os.rename(i,new_name)

# 类和对象、烤红薯
# class Potato():
#     def __init__(self):
#         self.state = '生的'
#         self.count_time = 0
#         self.flavs = []
#
#     def make_potato(self,time):
#         self.count_time += time
#         if 0 <= self.count_time < 3:
#             self.state = '生的'
#         elif 3 <= self.count_time <6:
#             self.state = '半生的'
#         elif 6 <= self.count_time <10:
#             self.state = '熟了'
#         else:
#             self.state = '熟过了'
#
#     def add_flav(self,flav):
#         self.flavs.append(flav)
#
#     def __str__(self):
#         return f'红薯考了{self.count_time}分钟，现在的状态是{self.state}，添加的调料有{self.flavs}'
#
#     def __del__(self):
#         print("红薯被销毁了")
#
# p1 = Potato()
# p1.make_potato(3)
# p1.add_flav('辣椒')
# p1.make_potato(8)
# p1.add_flav('白糖')
# print(p1)

# 房子和家具
# class Item():
#     def __init__(self,name,area):
#         self.name = name
#         self.area = area
#
#
#
# class Home():
#     def __init__(self,position,area):
#         self.position = position
#         self.area = area
#         self.now_area = area
#         self.items = []
#
#     def add_item(self,item):
#         if self.now_area > item.area:
#             self.items.append(item.name)
#             self.now_area = self.now_area - item.area
#         else:
#             print('房间位置不够')
#
#     def __str__(self):
#         return f'房间位置处于{self.position}，房间大小为{self.area}平方米，内置家具有{self.items}，剩余未利用面积为{self.now_area}'
#
# item1 = Item('床',30)
# item2 = Item('沙发',100)
# item3 = Item('电脑',50)
# home = Home('天津市 河西区 天津职业技术师范大学',150,)
# home.add_item(item1)
# home.add_item(item2)
# home.add_item(item3)
#
# print(home)
# 继承
# class Father(object):
#     def __init__(self):
#         self.content = '[祖传秘方]'
#         print("Father类中的init方法调用")
#
#     def use_content(self):
#         print(f'使用祖传的{self.content}做煎饼')
#
#     def __str__(self):
#         return 'Father类'
#
# class School(object):
#     def __init__(self):
#         self.content = '[学校科学秘方]'
#         print('School类中的init方法调用')
#
#     def use_content(self):
#         print(f'使用学校的{self.content}制作煎饼')
#
#
#
# class Son(School,Father):
#     # def __init__(self):
#     #     self.content = '[自研秘方]'
#     #     self.use_content()
#     #     print(self)
#     def __init__(self):
#         self.content = '[自研秘方]'
#
#     def use_content(self):
#         print(f'使用自己研发的{self.content}制作煎饼')
#
#     def use_School_content(self):
#         School.__init__(self)
#         School.use_content(self)
#
# son = Son()
# Father.__init__(son)
# Father.use_content(son)

# 单继承
# class School(object):
#     def __init__(self):
#         self.content = '学校科学秘方'
#
#     def use_content(self):
#         print(f'使用学校的{self.content}制作煎饼')
#
# class Father(School):
#     def __init__(self):
#         self.content = '祖传秘方'
#
#     def use_content(self):
#         print(f'使用祖传的{self.content}制作煎饼')
#         super().__init__()
#         super().use_content()
#
# class Son(Father):
#     def __init__(self):
#         self.content = '自研秘方'
#
#     def use_content(self):
#         print(f'使用自研的{self.content}制作煎饼')
#
#     def use_father_content(self):
#         # Father.__init__(self)
#         # Father.use_content(self)
#         # super(Son,self).__init__()
#         # super(Son,self).use_content()
#         super().__init__()
#         super().use_content()
#
#     def use_school_content(self):
#         # School.__init__(self)
#         # School.use_content(self)
#         pass
#
# son = Son()
# son.use_father_content()

# 私有属性
# class School(object):
#     def __init__(self):
#         self.able = '制作煎饼'
#         self.__money = 2000
#     def make_more(self):
#         print(f'批量{self.able}')
#     def get_money(self):
#         return self.__money
#     def set_money(self,money):
#         self.__money = money
#
# class Student(School):
#     pass
#
#
# s = Student()
# print(s.able)
# s.make_more()
# print(s.get_money())
# s.set_money(18000)
# print(s.get_money())

# 多态
# class Dog(object):
#     def able(self):
#         print("嚎叫")
#
# class CatDog(Dog):
#     def able(self):
#         print("抓捕")
#
# class BreakDog(Dog):
#     def able(self):
#         print("跳跃")
#
# dog = Dog()
# dog.able()
# choose = 1
# if choose == 10:
#     dog = CatDog()
# else:
#     dog = BreakDog()
# dog.able()

# 类属性类方法
# class Dog(object):
#     count = 0
#     __weakness = '腰'
#     @classmethod
#     def get_weakness(cls):
#         print(cls.__weakness)
#
#     @staticmethod
#     def print_info():
#         print('谁都可以用，不涉及类和对象的传递')
#     @staticmethod
#     def print_info2(name):
#         print(f'{name}谁都可以用，不涉及类和对象的传递')
#
#     def __init__(self,name):
#         Dog.count += 1
#         self.name = name
#
#     def able(self):
#         print("嚎叫")
#
# d1 = Dog('dog1')
# d2 = Dog('dog2')
# print(Dog.count)
# Dog.count = 5
# d1.count = 4
# print(d1.count)
# print(d2.count)
# Dog.get_weakness()
# d1.get_weakness()
# d1.able()
# Dog.able(d2)
# d1.print_info()
# Dog.print_info()
# d1.print_info2("d1")
# Dog.print_info2("Dog")

# 异常的使用
# try:
#     file = open('test.p','r')
# except:
#     print("出错了，找不到文件")
#     file = open('test.p','w')
# else:
#     print("执行正确")
# finally:
#     print('完成一次测试')

# try:
#     open('cctv1')
# except (FileExistsError,NameError,FileNotFoundError) as result:
#     print(result)

# 自定义异常

# class ShortInputException(Exception):
#
#     def __init__(self,provide):
#         self.provide = provide
#
#     def __str__(self):
#         return f'密码长度太短,小于{self.provide}'
#
# try:
#     provide = 3
#     pwd = input('请设置你的密码\n')
#     if len(pwd) < provide:
#         raise ShortInputException(provide)
# except Exception as result:
#     print(result)
# else:
#     print('设置成功')

# 导包/导模块
# import test_module1
# test_module1.print_info1()
# import test_module1 as t
# t.print_info1()
# from test_module1 import print_info1 as p
# # print_info1()
# p()
# from test_module1 import *
# # import test_module1
# print_info1()
# from test_module1 import print_info1,sum
# sum(1,2)
# print_info1()

# import random
# print(random.randint(3,5))

# from test_module1 import print_info as p1
# from test_module2 import print_info as p2
# p1()
# p2()

# import demo.my_module1
# demo.my_module1.add(1,2)
# from demo import my_module1,my_module2
#
# my_module1.add(2, 3)
# my_module2.sum(2,3)

# from demo import *
# my_module2.sum(1,2)
# my_module1.add(1,2)

# from test_module1 import *
# import test_module1
#
# dog = test_module1.Dog()
# print(test_module1.name)

# __dict__函数
# class Dog(object):
#     a = 1
#
#     def __init__(self):
#         self.name = 'lisa'
#
#     def jk(self):
#         print('aaaa')
#
#     @classmethod
#     def kk(cls):
#         pass
#     @staticmethod
#     def hh():
#         pass
# dog = Dog()
#
# print(Dog.__dict__)
# print(dog.__dict__)








