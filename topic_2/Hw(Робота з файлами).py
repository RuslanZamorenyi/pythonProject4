# Завдання 1
# Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел.
# Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.


# with open("file.txt", "w") as f1:
#     for i in range(1000):
#         f1.write(f'{str(i)} \n')
#
#
#
# with open("files.txt", "r") as f:
#     result = sum(map(float, f))
# print(result)

# Завдання 2
# Модифікуйте вихідний код сервісу зі скорочення посилань із попередніх двох уроків так, щоб він зберігав базу посилань
# на диску і не «забув» при перезапуску



# Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл
# with open("fil.txt", "a") as f1:
#     my_list = [1, 2, 5, 8, 10, 11, 18]
#     list1 = []
#     for a in my_list:
#         if a % 2:
#             continue
#         else:
#             list1.append(a)
#     list2 = [a ** 2 for a in list1]
#     print(list2)
#     f1.write(f'{str(list2)} \n')


# with open("fil.txt", "a") as f1:
#     list1 = (x ** 2 if x // 2  else x for x in range (0, 100, 2))
#     print(list(list1))
#     f1.write(f'{str(list1)} \n')



# Опишіть клас співробітника, який вміщує такі поля: імя, прізвище, відділ і рік початку роботи. Конструктор
# має генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із клавіатури. Виведіть усіх
# співробітників, які були прийняті після цього року.


# with open("fil.txt", "a") as f1:
#     class Employee:
#         LIST_EMPLOYEE = []
#         def __init__(self, name, surname, department, year, LIST_EMPLOYEE = LIST_EMPLOYEE):
#             try:
#
#                 if type(name) != str:
#                     raise ValueError("name mast be string")
#                 else:
#                     self.name = name
#
#                 if type(surname) != str:
#                     raise ValueError("name must be string")
#                 else:
#                     self.surname = surname
#
#                 if type(department) != str:
#                     raise ValueError("name must be string")
#                 else:
#                     self.department = department
#
#                 if type(year) != int and 1995<year<2022:
#                     raise ValueError("year is wrong")
#                 else:
#                     self.year = year
#
#                 LIST_EMPLOYEE.append({"name": self.name, "surname": self.surname, "department": self.department,
#                                       "year": self.year})
#
#             except Exception as e:
#                 print(e)
#
#         def fun(self, year, LIST_EMPLOYEE = LIST_EMPLOYEE):
#             for i in LIST_EMPLOYEE:
#                 if i["year"] > year:
#                     print(i)
#                     f1.write(f'{str(i)} \n')
#
#
#
#     new_employee = Employee("maks", "mask", "engineer", 2010)
#     new_employee1 = Employee("makss1", "mask1", "engineer", 2007)
#     new_employee2 = Employee("makks2", "mask2", "engineer", 1912)
#     new_employee3 = Employee("mafks3", "mask3", "engineer", "fdsf")
#     new_employee.fun(2005)