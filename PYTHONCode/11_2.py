class Queue():
    def __init__(self,maxlen) -> None:       
        self.maxlen = maxlen                 #队列最大长度
        self.doubleq = []                    #空队列
    def insertLeft(self,value):              #左端插入元素value
        if len(self.doubleq)==self.maxlen:   #判断队列是否满
            return False
        else:
            self.doubleq.insert(0,value)
            print("左插元素成功--------------------")
    def insrtRight(self,value):              #右端插入元素value
        if len(self.doubleq)==self.maxlen:
            return False
        else:
            self.doubleq.append(value)
            print("右插元素成功--------------------")
    def deleteLeft(self):                    #左端删除value
        if len(self.doubleq)==0:             #判断队列是否为空
            return False
        else:
            self.doubleq.pop(0)
            print("左删元素成功--------------------")
    def deleteRight(self):                   #右端删除value
        if len(self.doubleq)==0:
            return False
        else:
            self.doubleq.pop()
            print("右删元素成功--------------------")
    def find(self,value): 
        if len(self.doubleq)==0:             #判断队列是否为空
            return False                     #查找value
        elif self.doubleq.index(value):
            print("找到元素",value,"--------------------")
    def Traverse(self):                      #遍历队列
        if len(self.doubleq)==0:             #判断队列是否为空
            return False
        else:
            for x in self.doubleq:
                print(x)
            print("遍历成功--------------------")
    def length(self):                        #求队列长度
        print("列表长度为：",len(self.doubleq))
        print("长度成功--------------------")
def main():
    q = Queue(50)
    print("原双端列表： ",q.doubleq)
    q.insertLeft(input("leftvalue: "))
    print("双端列表： ",q.doubleq)
    q.insrtRight(input("rightvalue: "))
    print("双端列表： ",q.doubleq)
    q.insertLeft(input("leftvalue: "))
    print("双端列表： ",q.doubleq)
    q.insrtRight(input("rightvalue: "))
    print("双端列表： ",q.doubleq)
    q.deleteLeft()
    print("双端列表： ",q.doubleq)
    q.deleteRight()
    print("双端列表： ",q.doubleq)
    q.find(input("findvalue: "))
    q.Traverse()
    q.length()
main()
