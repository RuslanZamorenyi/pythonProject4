# Завдання 1
# Вивчіть основні стандартні винятки, які перераховані в цьому уроці

# Завдання 2
# Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення, ділення та піднесення до
# ступеня. Програма має видавати повідомлення про помилку та продовжувати роботу під час введення некоректних даних,
# діленні на нуль та зведенні нуля в негативний степінь.

# a = input("введіть вид операціі\n\tдодавання\n\tвіднімання\n\tмноження\n\tділення\n\tпіднесення до ступеня\nвибір:")
#
# if a == "множення":
#
#
#     b = float(input("введіть перше число:"))
#     c = float(input("введіть друге число:"))
#     print(b * c)
# elif a == "ділення":
#     d = float(input("введіть перше число:"))
#     while True:
#         e = float(input("введіть друге число:"))
#         try:
#             e != 0
#             print(d / e)
#             break
#         except:
#             print("помилка! на нуль ділити не можна")
#
# elif a == "віднімання":
#     f = float(input("введіть перше число:"))
#     h = float(input("введіть друге число:"))
#     print(f - h)
#
# elif a == "додавання":
#     g = float(input("введіть перше число:"))
#     t = float(input("введіть друге число:"))
#     print(g + t)
#
# elif a == "піднесення до ступеня":
#     w = float(input("введіть число:"))
#     while True:
#         # w = float(input("введіть число:"))
#         v = float(input("введіть ступінь:"))
#         if w == 0:
#             try:
#                 v > 0
#                 print(w ** v)
#                 break
#             except:
#                 print("помилка! ступінь не може буді відєина ")
#         else:
#             print(w ** v)
#             break

# Завдання 3
# Опишіть клас співробітника, який вміщує такі поля: імя, прізвище, відділ і рік початку роботи. Конструктор
# має генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із клавіатури. Виведіть усіх
# співробітників, які були прийняті після цього року.



class Employee:
    LIST_EMPLOYEE = []
    def __init__(self, name, surname, department, year, LIST_EMPLOYEE = LIST_EMPLOYEE):
        try:

            if type(name) != str:
                raise ValueError("name mast be string")
            else:
                self.name = name

            if type(surname) != str:
                raise ValueError("name must be string")
            else:
                self.surname = surname

            if type(department) != str:
                raise ValueError("name must be string")
            else:
                self.department = department

            if type(year) != int and 1995<year<2022:
                raise ValueError("year is wrong")
            else:
                self.year = year

            LIST_EMPLOYEE.append({"name": self.name, "surname": self.surname, "department": self.department,
                                  "year": self.year})

        except Exception as e:
            print(e)

    def fun(self, year, LIST_EMPLOYEE = LIST_EMPLOYEE):
        for i in LIST_EMPLOYEE:
            if i["year"] > year:
                print(i)



new_employee = Employee("maks", "mask", "engineer", 2010)
new_employee1 = Employee("makss1", "mask1", "engineer", 2007)
new_employee2 = Employee("makks2", "mask2", "engineer", 1912)
new_employee3 = Employee("mafks3", "mask3", "engineer", "fdsf")
new_employee.fun(2005)
