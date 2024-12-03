
from student import *
class SystemStudentManage(object):
    def __init__(self):
        self.sudents = []
        self.FILE_NAME = 'students.data'

    def run(self):
        self.load_info()
        while(True):
            self.print_menu()
            choose = int(input('请选择你要操作的项目'))
            if choose == 1:
                self.add_student()
                print('添加成功')
            elif choose == 2:
                self.del_student()
                print('操作成功')
            elif choose == 3:
                self.find_student()
                print('操作成功')
            elif choose == 4:
                self.find_all_student()
                print('查找到所以学生')
            elif choose == 5:
                self.update_student()
                print('修改成功')
            elif choose == 6:
                self.exit_and_save()
                print('保存退出成功')
                break
    def print_menu(self):
        print('''1.添加学生
                 2.删除学生
                 3.查找学生
                 4.查看所有学生
                 5.修改学生
                 6.保存并退出系统''')

    def add_student(self):
        name = input('请输入学生姓名')
        age = input('请输入学生年龄')
        tel = input('请输入学生联系方式')
        stu = Student(name,age,tel)
        self.sudents.append(stu)

    def del_student(self):
        name = input('请输入学生的名字')
        for s in self.sudents:
            if s.name == name:
                self.sudents.remove(s)
                break
        else:
            print('没有该学生')

    def find_student(self):
        name = input('请输入学生的名字')
        for s in self.sudents:
            if s.name == name:
                print(s)
                break
        else:
            print('没有该学生')

    def find_all_student(self):
        for s in self.sudents:
            print(s)

    def update_student(self):
        name = input('请输入你需要修改的学生姓名')
        for s in self.sudents:
            if s.name == name:
                new_name = input('请输入新的学生姓名')
                new_age = input('请输入新的学生年龄')
                new_tel = input('请输入新的学生联系方式')
                s.name = new_name
                s.age = new_age
                s.tel = new_tel
                break
        else:
            print('没有该学生')

    def exit_and_save(self):
        file = open(self.FILE_NAME,'w')
        save_arr = []
        for s in self.sudents:
            save_arr.append(s.__dict__)
        file.write(str(save_arr))

    def load_info(self):
        try:
            file = open(self.FILE_NAME,'r')
        except:
            file = open(self.FILE_NAME,'w')
        else:
            load_arr = (file.read())
            print(load_arr)
        finally:
            file.close()


