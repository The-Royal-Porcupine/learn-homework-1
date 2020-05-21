"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

import sys


def ask_user():
    # Она будет, как и предыдущая, спрашивать Как дела, пока не получит ответ Хорошо
    # И, если получит вопрос, ответ на который знает - ответит и снова спросит Как дела

    try:

        phrases = {'как дела?': 'Отлично!', 'что делаешь?': 'Программирую', 'партия?': 'Жуликов и воров',
                   'спорт?': 'Ты мир'}
        answer = input("Как дела? ")
        while answer.lower() != 'хорошо':
            print(phrases.get(answer.lower(), ''))
            answer = input("Как дела? ")

    except KeyboardInterrupt:

        print("Пока!")
        sys.exit()

    # А как сделать с break?


if __name__ == "__main__":
    ask_user()
