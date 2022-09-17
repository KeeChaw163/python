class Num():
    def __init__(self,a) -> None:
        self.a = a
    def sNum(self):  
        for x in (str,list,tuple,dict,set,None):  #不是数值类型
            if isinstance(self.a,x):              #判断类型不是数值型
                raise TypeError  
            elif self.a>=0:                       #如果a>=0,返回原数
                self.result = self.a
                return self.result
            elif self.a<0:                        #如果a<0,返回相反数
                self.result = -self.a
                return self.result 
    def error(self):                          #定义测试异常方法
        try:                                  #捕获异常
            num = Num()
            num.sNum()
        except TypeError as e:                #处理异常，打印输出提示
            print("输入错误：不是数值类型！！！！！")