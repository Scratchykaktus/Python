#Поле first — целое положительное число, часы; поле second — 
# целое положительное число, минуты. Реализовать метод 
# minutes() — приведение времени в минуты.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Time():
    
    def __init__(self, first = 0, second = 0):
        self.__first = int(first)
        self.__second = int(second)

    def get_first(self):
        return self.__first
    
    def set_first(self, f):
        self.__first = f

    def get_second(self):
        return self.__second

    def set_second(self, s):
        self.__second = s

    def minutes(self):
        return self.__second + (self.__first * 60)
    
    #ввод с клавиатуры
    def read(self):
        self.set_first(int(input("Введите кол-во часов: ")))
        self.set_second(int(input("Введите кол-во минут: ")))

    #вывод на экран
    def display(self):
        print(f'Кол-во минут: {self.minutes()}')

if __name__ == '__main__':
    time = Time()
    time.read()
    time.display()
