from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, nam_, pow_):
        Thread.__init__(self)
        self.nam_ = nam_
        self.pow_ = pow_

    def run(self):
        print(f"{self.nam_}, на нас напали!")
        enems_ = 100
        days_ = 0
        while enems_:
            enems_ -= self.pow_
            days_ += 1
            print(f"{self.nam_} сражается {days_} дней..., осталось {enems_} воинов.")
            sleep(1)
        print(f"{self.nam_} одержал победу спустя {days_} дней.\n")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()



