class MyClass(object):
    i=123456               #定义类成员i，初始化为123456
    def f(self):           #方法或称为类中的函数
        return MyClass.i
x=MyClass()                #创建MyClass类的对象，并赋值给x

print(x.f())               #使用对象x调用该类的f()函数

print(x.i)
            
        
            