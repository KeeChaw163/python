class Person(object): #必须以object为基类 
    def __init__(self, name , age , sex ) -> None:
        self.setName(name) 
        self.setAge(age) 
        self.setSex(sex)
    def setName(self,name):
        if not isinstance(name,str):
            print('name must be string.')
            return
        self.__name = name
    def setAge(self,age):
        if not isinstance(age, int):
            print('age must be integer.')
            return
        self.__age = age
    def setSex(self,sex):
        if sex not in('man', 'woman'):
            print('sex must be "man" or "woman"')
            return
        self.__sex=sex
    def show(self):
        print('Name:',self.__name) 
        print('Age:',self.__age)
        print('Sex:', self.__sex)
class Teacher(Person): #派生类 
    def __init__(self, name, age, sex, department) -> None:
        super().__init__(name=name, age=age, sex=sex)
        ## or, use another method like below:
        #Person.__init__(self, name, age, sex) 
        self.setDepartment(department)
    def setDepartment(self,department):
        if not isinstance(department, str):
            print('department must be a string.')
            return
        self.__department=department
    def show(self):
        super(Teacher,self).show()
        print('Department:',self.__department)
class Student(Person): #派生类
    def __init__(self, name, age, sex, major) -> None:
        super().__init__(name=name, age=age, sex=sex)
        self.setMajor(major)
    def setMajor(self,major):
        if not isinstance(major, str):
            print('department must be a string.')
            return
        self.__major=major
    def show(self):
        super(Student,self).show()
        print('Major:',self.__major)
if __name__ == '__main__':
    zhangsan = Person('Zhang San', 19, 'man') 
    print('Person.show: --------------------')
    zhangsan.show()
    lisi = Teacher('Li Si',32,'man','Math') 
    print('Teacher.show: --------------------')
    lisi.show()
    tom = Student('Tom',21,'woman','Big Data')
    print('Student.show: --------------------')
    tom.show()

