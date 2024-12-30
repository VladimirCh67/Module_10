from threading import Thread, Lock
from time import sleep
from random import randint

lock = Lock()
class Bank:
    def __init__(self):
        self.balance = 0


    def deposit(self):
        for i in range(100):
            x = randint(50, 500)
            self.balance += x
            print(f"Пополнение: {x}. Баланс: {self.balance}")
            #if self.balance >= 500 and lock.locked():
            if lock.locked():
                lock.release()

            sleep(0.01)


    def take(self):
        for i in range(100):
            x = randint(50, 500)
            print(f"Запрос на {x}")
            if x <= self.balance:
                self.balance -= x
                print(f"Снятие: {x}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств" )
                lock.acquire()

            sleep(0.01)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

