class Users():
    def __init__(self, name, major,banji):
        self.name = name
        self.major = major
        self.banji = banji 
    def setAge(self, age):
        if isinstance(age,int):
            if age >= 0 and age <= 100:
                self.age = age
            else:
                raise AgeInputException
        else:
            raise AgeInputException
    def setSex(self, sex):
        if sex == '男' and '女':
            self.sex = sex
        else:
            raise SexInputException
class InputException(Exception):
    pass
class SexInputException(InputException):
    message = "性别输入有误，sex只有男、女！！！！！"
class AgeInputException(InputException):
    message = "年龄输入有误，age在0-100，并且为整数！！！！！"
def main():
    try:
        name = input("name: ")
        major = input("major: ")
        banji = input("banji: ")
        user = Users(name, major,banji)
        age = int(input("age: "))
        user.setAge(age)
        sex = input("sex: ")
        user.setSex(sex)
    except AgeInputException as e1:
        print(e1.message)
    except SexInputException as e2:
        print(e2.message)
    finally:
        print("程序结束！！！！！")
main()