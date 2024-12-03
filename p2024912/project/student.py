class Student(object):
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return f'学生姓名{self.name},学生年龄{self.age},学生联系方式{self.tel}'