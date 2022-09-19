# Завдання 1
# Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи ThreadPoolExecutor,
# і заміряйте швидкість їхнього виконання, а потім заміряйте швидкість обчислення, використовуючи той же набір завдань
# на ProcessPoolExecutor. Як приклади використовуйте останні значення, від мінімальних і до максимально можливих, щоб
# побачити приріст або втрату продуктивності.
# import threading
# import time
#
#
# def fun(start=1, end=0):
#     result = 0
#     for i in range(start, end):
#         result += i
#     print("number =", result)
#
#
# number = {"end": 45}
#
# task = threading.Thread(target=fun, kwargs=number)
# started_at = time.time()
# print("Result 1")
# task.start()
#
# task.join()
# result_1 = time.time() - started_at
# print("Time is", result_1)
# started_at = time.time()
#
# print("Result 2")
# fun(**number)
# finish_time = time.time()
# result_2 = finish_time - started_at
# print("Time is", result_2)


# Завдання 2
# Створіть три функції, одна з яких читає файл на диску із заданим імям та перевіряє наявність рядка «Wow!». Якщо файлу
# немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу. Якщо файл є, то відкриває його і шукає рядок
# «Wow!». За наявності цього рядка закриває файл і генерує подію, а інша функція чекає на цю подію і у разі її виникнення
# виконує видалення цього файлу. Якщо рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд. Створіть файл руками
# та перевірте виконання програми.

from __future__ import print_function
import io
import time


def fun_1():
    word = "Wow!"
    check = find_function(word)
    if check:
        find_function()
        del_function()
    else:
        time_function()


def find_function(word):
    with io.open("file1_1.txt", "r", encoding="utf-8") as f:
        text = f.read()
        for line in text:
            if word in line:
                return True
    return False


def del_function():
    with open("file1_1.txt", "r") as f:
        data = f.readlines()

    data = filter(lambda line: "Wow!" not in line, data)


def time_function():
    time.sleep(5)
    print("file don`t find!!!")
