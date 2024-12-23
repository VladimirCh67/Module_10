import threading
from threading import Thread
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            x = "Какое-то слово № " + str(i) + "\n"
            file.write(x)
            print(i, file_name)
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


# write_words(10, "example1.txt")
# write_words(30, "example2.txt")
# write_words(200, "example3.txt")
# write_words(100, "example4.txt")

thread1 = Thread(write_words(10, "example5.txt"))
thread2 = Thread(write_words(30, "example6.txt"))
thread3 = Thread(write_words(200, "example7.txt"))
thread4 = Thread(write_words(100, "example8.txt"))


write_words(10, "example1.txt")
thread1.start()
thread1.join()
thread2.start()
thread3.start()
thread4.start()