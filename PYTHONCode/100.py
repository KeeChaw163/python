import threading
from threading import Thread, Condition,Lock

class BankUser:
    # 账户初始化
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.lock = Lock()

    def draw_money(self, draw_amount):
        global  draw_count
        self.lock.acquire()
        try:
            if self.__balance < draw_amount:
                print("%s  余额不足"%threading.currentThread().name)
            else:
                print(threading.currentThread().name + "取钱" + str(draw_amount))
                self.__balance = self.__balance - draw_amount
                draw_count+=1

        finally:
            self.lock.release()