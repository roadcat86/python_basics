"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]

user_num = None

response = input("Наполним БД рейтингом? (Да/Нет): ")
while user_num != "СТОП":
    if response.lower() == 'нет':
        print('Ну ладно, пока...')
        break
    elif response.lower() == 'да':
        print("Если хотите остановаиться - введите вместо числа 'СТОП'")
        user_num = input("Введите целое число: ")
        if user_num != 'СТОП':
            my_list.append(int(user_num))
            my_list.sort()
            print(my_list[::-1])
    else:
        print("Вы что-то не то ввели... Давайте еще раз!")
        response = input("Наполним БД рейтингом? (Да/Нет): ")

print(f"Итого у нас такой порядок: {my_list[::-1]}")
