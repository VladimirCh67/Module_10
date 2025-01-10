from threading import Thread
from random import randint
from time import sleep
from queue import Queue

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.q = Queue()

    def guest_arrival(self, *guests):
        #self.guests = guests
        for g_name in guests:
            for num in range(1, 6):
                if Table(num).guest is None:
                    Table(num).guest = g_name
                    Guest(g_name).start()
                    print(f"{g_name} сел(-а) за стол номер {num}")



    def discuss_guests(self):
        while not self.q.empty():
            for num in range(1, 6):
                if Table(num).guest is not None:
                    if Guest(Table(num).guest).is_alive():
                        print(f"{Guest(Table(num).guest)} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {num} свободен")
                        Table(num).guest = None
                



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
