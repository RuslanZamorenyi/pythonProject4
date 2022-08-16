# Завдання 1
# Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed
# my_list = [1, 2, 5, 8, "jdcjdk"]
# generator = (a for a in my_list[::-1])
# print(list(generator))


# Завдання 2
# Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл
# my_list = [1, 2, 5, 8, 10, 11, 18]
# list1 = []
# for a in my_list:
#     if a % 2:
#         continue
#     else:
#         list1.append(a)
# list2 = [a ** 2 for a in list1]
# print(list2)


# list1 = (x ** 2 if x // 2  else x for x in range (0, 100, 2))
# print(list(list1))
