#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def input_data(list_route):
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
    
    list_route.append(route)

    return list_route

def output_data(list_route):
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