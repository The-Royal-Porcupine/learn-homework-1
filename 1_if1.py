"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main(age):

    if 0 < age < 7:
        return "Детский сад"
    elif 7 <= age < 18:
        return "Школа"
    elif 7 <= age < 18:
        return "ВУЗ"
    elif 19 <= age <= 60:
        return "Работа"
    else:
        return "Нет предположений"


if __name__ == "__main__":
    age = input("Сколько Вам полных лет? ")
    if age.isdigit():
        print("Вероятное занятие: " + main(int(age)))
    else:
        print("Неверный формат ввода")
