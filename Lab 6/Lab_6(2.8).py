#Решить индивидуальное задание лабораторной работы 2.6, оформив каждую команду в виде отдельной функции.
#Ключи: название начального пункта маршрута; название конечного пункта маршрута; 
#номер маршрута. Ввод с клавиатуры данных в список, записи упорядочены по 
#номерам маршрутов. Вывод маршрута номер которого ввели с клав. , если нет - сообщить

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from os import sep

if __name__ == '__main__':

    list_route = []

    def input_data():
        #Ввод данных с клавиатуры
        start_point = input("Введите начальный пункт маршрута: ")
        end_point = input("Введите конечный пункт маршрута: ")
        number_route = int(input("Введите номер маршрута: "))
        
        print("Маршрут добавлен!\n")
        input("Нажмите 'Enter' для продолжения")
        #Создание словаря "Маршрут"
        route = {
            'start_point': start_point, 
            'end_point': end_point,
            'number_route': number_route
        }

        #Добавление маршрута в список
        global list_route
        list_route.append(route)

    def output_data():
        if len(list_route) == 0:
            print("Ваш список пуст! Сначала добавьте маршруты в список!\n")
            input("Нажмите 'Enter' для продолжения")
        else:
            #Сортировка списка по номеру маршрутов
            list_route.sort(key=lambda item: item.get('number_route'))

            #Вывод
            for i, route in enumerate(list_route, 1):
                print(i,".",
                    " Начальный пункт: ",route.get('start_point', ''),";",
                    " Конечный пункт: ",route.get('end_point', ''),";",
                    " Номер маршрута: ",route.get('number_route', 0),";",
                    sep=''
                    )
            print()
            input("Нажмите 'Enter' для продолжения")

    while True:
        os.system('cls')
        print("Заполнить список >> [1]")
        print("Вывод списка >> [2]")
        print("Выход >> [3]")
        
        command = int(input(">>"))
        
        if command == 1:
            input_data()

        elif command == 2:
            output_data()

        elif command == 3:
            break
        else:
            print(f"Неизветсная команда: {command}\n")
            input("Нажмите 'Enter' для продолжения")
        
        