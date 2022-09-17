import unittest
from demo_class import Num
class classTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cs1 = Num(1.3)            #输入正数
        self.cs2 = Num(-0.99)          #输入负数
        self.cs3 = Num(0)              #输入0
        self.cs4 = Num({})             #输入非数值类型
    def tearDown(self) -> None: 
        pass
    def test_sNum(self):
        result1 = self.cs1.sNum()
        result2 = self.cs2.sNum()
        result3 = self.cs3.sNum()
        result4 = self.cs4.error()
        self.assertEqual(result1,1.3)  #期待返回值与输入相同
        self.assertEqual(result2,0.99) #期待返回值与输入相反
        self.assertEqual(result3,0)    #期待返回0
        self.assertEqual(result4,None) #期待抛出TypeError
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(classTest('test_sNum'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
