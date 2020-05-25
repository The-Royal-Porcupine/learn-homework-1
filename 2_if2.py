"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main(string_one, string_two):

    if type(string_one) == str and type(string_two) == str:
        if len(string_one) == len(string_two):
            return 1
        #далее все что попадет в else будет удовл-ть len(string_one) != len(string_two) - можно условие не писать
        elif  string_two == 'learn':
            return 3
        elif len(string_one) > len(string_two):
            return 2
        elif len(string_one) != len(string_two):
            return "Строки разной длины, и вторая длинее ^^"
    else:
        return "0"


if __name__ == "__main__":

    string_one = input("Введите первую строку: ")
    string_two = input("Введите вторую строку: ")
    print(main(string_one, string_two))

