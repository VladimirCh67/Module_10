from threading import Thread
from random import randint
from time import sleep
from queue import Queue

class Table:
    def __init__(self, number, n_guest = None):
        self.number = number
        self.n_guest = n_guest


class Guest(Thread):
    def __init__(self, name, tabl_ = False, que_ = False):
        Thread.__init__(self)
        self.name = name
        self.tabl_ = tabl_
        self.que_ = que_

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.q = Queue()

    def guest_arrival(self, *guests):
        self.guests = guests
        #for g_name in guests_names:
        for guest_ in self.guests:
            g_name = guest_.name
            print(g_name, guest_.tabl_, guest_.que_)
            if not guest_.tabl_ and not guest_.que_:
                for num in range(1, 6):
                    table_ = Table(num)
                    print(table_.number, table_.n_guest, ' до')
                    if table_.n_guest is None:
                        table_.n_guest = g_name
                        guest_.tabl_ = True
                        guest_.start()
                        #Guest(g_name).start()
                        print(f"{g_name} сел(-а) за стол номер {num}")
                        print(table_.number, table_.n_guest)
                        break

                print(g_name, guest_.tabl_, guest_.que_)


    def discuss_guests(self):
        while not self.q.empty():
            for num in range(1, 6):
                table_ = Table(num)
                if table_.n_guest is not None:
                    if Guest(table_.n_guest).is_alive():
                        print(f"{Guest(table_.n_guest)} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {num} свободен")
                        table_.n_guest = None
                



# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
