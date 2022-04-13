#Выполнить индивидуальное задание лабораторной работы 2.8, оформив все 
# классы программы в виде отдельного пакета. Разработанный пакет должен 
# быть подключен в основную программу с помощью одного из вариантов 
# команды import .
#Ключи: название начального пункта маршрута; название конечного пункта маршрута; 
#номер маршрута. Ввод с клавиатуры данных в список, записи упорядочены по 
#номерам маршрутов. Вывод маршрута номер которого ввели с клав. , если нет - сообщить

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from my_package import Data
from os import sep

if __name__ == '__main__':

    list_route = []

    while True:
        os.system('cls')
        print("Заполнить список >> [1]")
        print("Вывод списка >> [2]")
        print("Выход >> [3]")
        
        command = int(input(">>"))
        
        if command == 1:
            list_route = Data.input_data(list_route)

        elif command == 2:
            Data.output_data(list_route)

        elif command == 3:
            break
        else:
            print(f"Неизветсная команда: {command}\n")
            input("Нажмите 'Enter' для продолжения")
        
        