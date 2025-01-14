from threading import Thread
from random import randint
from time import sleep
from queue import Queue

class Table:
    def __init__(self, number, n_guest = None):
        self.number = number
        self.n_guest = n_guest


class Guest(Thread):
    def __init__(self, name, tabl_ = False):
        Thread.__init__(self)
        self.name = name
        self.tabl_ = tabl_

    def run(self):
        sleep(randint(1, 5))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.q = Queue()

    def guest_arrival(self, *guests):
        self.guests = guests
        for guest_ in self.guests:
            g_name = guest_.name
            if not guest_.tabl_:
                for table_ in tables:
                    if table_.n_guest is None:
                        table_.n_guest = g_name
                        guest_.tabl_ = True
                        guest_.start()
                        print(f"{g_name} сел(-а) за стол номер {table_.number}")
                        break

                if not guest_.tabl_:
                    self.q.put(guest_)
                    print(f"{g_name} в очереди")



    def discuss_guests(self):
        y = True
        while y:
            for guest_ in self.guests:
                if not guest_.tabl_:
                    continue
                if guest_.is_alive():
                    continue
                else:
                    nam_g = guest_.name
                    for table_ in tables:
                        if table_.n_guest == nam_g:
                            print(f"{nam_g} покушал(-а) и ушёл(ушла)")
                            print(f"Стол номер {table_.number} свободен")
                            table_.n_guest = None
                            if not self.q.empty():
                                g_name = self.q.get().name
                                table_.n_guest = g_name
                                for guest_2 in self.guests:
                                    if guest_2.name == g_name:
                                        guest_2.tabl_ = True
                                        guest_2.start()
                                        break
                                print(f"{g_name} вышел(-ла) из очереди и сел(-а) за стол номер {table_.number}")
                                break
                    guest_.tabl_ = False
            x = False
            for table_ in tables:
                if table_.n_guest is not None:
                    x = True
            if not x:
                y = False



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
