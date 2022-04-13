#Реализовать класс Account, представляющий собой банковский счет. 
# В классе должны быть четыре поля: фамилия владельца, номер счета, процент начисления
#  и сумма в рублях.
#Открытие нового счета выполняется операцией инициализации. Необходимо выполнять 
# следующие операции: сменить владельца счета, снять некоторую сумму денег со счета, 
# положить деньги на счет, начислить проценты, перевести сумму в доллары, перевести сумму
#  в евро, получить сумму прописью (преобразовать в числительное).

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from my_package import Num2Text

class Account():

    usd = 112 # Курс доллара
    eur = 122 # Курс евро

    def __init__(self, SecondName = "Иванов", AccountNumber = 4578, PrecAcc = 10.2, AmountRub = 5848):
        self.__SecondName = SecondName          # Фамилия владельца
        self.__AccountNumber = AccountNumber    # Номер счета
        self.__PrecAccrual = PrecAcc            # Процент начисления
        self.__AmountRub = float(AmountRub)     # Сумма в рублях

    def get_name(self):
        return self.__SecondName

    def set_name(self, n):
        self.__SecondName = n

    def get_accnumber(self):
        return self.__AccountNumber
    
    def set_accnumber(self, number):
        self.__AccountNumber = number

    def get_prec(self):
        return self.__PrecAccrual

    def set_prec(self, prec):
        self.__PrecAccrual = prec

    def get_rub(self):
        return self.__AmountRub

    def set_rub(self, rub):
        self.__AmountRub = rub

    # Смена владельца счета
    def change_name(self):
        self.set_name(input("Введите фамилию нового владельца: "))

    # Снятие денег со счета
    def take_money(self):
        print("Сумма на счету:", self.get_rub())
        amount_entered = float(input("Введите сумму денег, которые хотите снять:")) 
        if amount_entered > self.get_rub():
            print(f"Вы не можете ввести сумму больше вашего счета: {self.get_rub()}")
            self.take_money()
        else:
            self.set_rub(self.get_rub() - amount_entered)
            print("Отстаток счета:", self.get_rub())

    # Зачисление денег на счет
    def give_money(self):
        print("Сумма на счету:", self.get_rub())
        amount_entered = float(input("Введите сумму денег, которые хотите зачислить:")) 
        self.set_rub(self.get_rub() + amount_entered)
        print("Сумма на счету:", self.get_rub())

    # Начисление процентов
    def add_perecent(self):
        print("Процент начисления:", self.get_prec())
        add_prec = float(input("Введите кол-во процентов, которые хотите начислить:"))
        self.set_prec(self.get_prec() + add_prec)
        print("Начисленные проценты:", self.get_prec())

    # Перевод суммы в доллары
    def conver_usd(self):
        print(f"Ваш счет в рублях: {self.get_rub()}")
        print(f"Ваш счет в долларах: {self.get_rub() / self.usd}")

    # Перевод суммы в евро
    def conver_eur(self):
        print(f"Ваш счет в рублях: {self.get_rub()}")
        print(f"Ваш счет в евро: {self.get_rub() / self.eur}")


    # Получение суммы прописью
    def sum_to_text(self):
        
        # 1 - 99
        if 0 < self.get_rub() < 100:
            print(Num2Text.do_sta(self.get_rub()), "рублей")
        # 100 - 999
        elif 99 < self.get_rub() < 1000:
            print(Num2Text.do_tisyachi(self.get_rub()), "рублей")
        # 1000 - 9999
        elif 999 < self.get_rub() < 10000:
            print(Num2Text.do_ten_tisyachi(self.get_rub()), "рублей")
        # 10000 - 99999
        #elif self.get_rub() < 100000:
            

    # Вывод на экран
    def display(self):
        print(f"Владелец счета: {self.get_name()}")
        print(f"Номер счета: {self.get_accnumber()}")
        print(f"Сумма счета: {self.get_rub()} руб.")
        print(f"Процент начисления: {self.get_prec()} %")

    # Ввод данных
    
if __name__ == '__main__':
    acc = Account()
    while True:
        os.system('cls')
        acc.display()
    
        print("\nСменить владельца счета >> [1]")
        print("Снять сумму денег со счета >> [2]")
        print("Пополнить счет>> [3]")
        print("Начислить проценты >> [4]")
        print("Перевести сумму в доллары >> [5]")
        print("Перевести сумму в евро >> [6]")
        print("Получить сумму прописью (до 9999) >> [7]")
        print("Выход >> [8]")
        
        command = int(input(">>"))
        
        if command == 1:
            acc.change_name()
            input()    
        elif command == 2:
            acc.take_money() 
            input() 
        elif command == 3:
            acc.give_money()
            input() 
        elif command == 4:
            acc.add_perecent() 
            input() 
        elif command == 5:
            acc.conver_usd() 
            input() 
        elif command == 6:
            acc.conver_eur() 
            input() 
        elif command == 7:
            acc.sum_to_text() 
            input() 
        elif command == 8:
            break
        else:
            print(f"Неизветсная команда: {command}\n")
            input("Нажмите 'Enter' для продолжения")    
    
    