"""
Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():

    marks_by_classes = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '5b', 'scores': [5, 4, 3, 3, 2]},
        {'school_class': '6a', 'scores': [3, 5, 5, 4, 2]},
        {'school_class': '7b', 'scores': [5, 5, 5, 2, 2]}
    ]

    pupils_number_total = 0
    scores_sum_total = 0
    for each_class in marks_by_classes:
        print(f"Средний балл в {each_class['school_class']}: {sum(each_class['scores']) / len(each_class['scores'])}")
    
    # так за средний бал считается только последний класс, потому что два этих действия - не в цикле
    # чтобы данные действия производились в цикле и результат был верным, нужно добавить отступы
        pupils_number_total += len(each_class['scores'])
        scores_sum_total += sum(each_class['scores'])
    print(f"Средний балл по школе: {scores_sum_total / pupils_number_total}")


if __name__ == "__main__":
    main()


