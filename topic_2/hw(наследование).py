# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document.
# Пусть метод edit_document выводит на экран информацию о том, что редактирование
# документов недоступно для бесплатной версии. Создайте подкласс ProEditor, в котором
# данный метод будет переопределён. Введите с клавиатуры лицензионный ключ и, если
# он корректный, создайте экземпляр класса ProEditor, иначе Editor. Вызовите методы
# просмотра и редактирования документов.

# class Editor:
#     TYPE = "edition1"
#     def __init__(self, information):
#         self.information = information
#
#
#     def edit_document(self):
#         print("{}".format(self.information))
#
#
#
# class ProEdition(Editor):
#     TYPE = "edition2"
#
#     def edit_document(self):
#         print("Congratulations you get key!!!!")
#
# edition = ProEdition("редагування документів не доступне в бесплатній версії")
# editions = [edition]
# for editor in editions:
#     editor.edit_document()


# Задание 2
# Опишите классы графического объекта, прямоугольника и объекта, который может
# обрабатывать нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного
# прямоугольника. Вызовите метод нажатия на кнопку.
class Rectangle:
    def __init__(self, name):
        self.name = name

class Button:
    def __init__(self, button):
        self.button = button

    def print_function(self, obj):
       print(obj)


rect = Rectangle('New')
butt = Button('print')

butt.print_function(rect.name)




# Задание 3
# Создайте иерархию классов с использованием множественного наследования. Выведите на экран порядок разрешения методов
# для каждого из классов. Объясните, почему линеаризации данных классов выглядят именно так

# class country:
#     TYPE = "Ukraine"
#
#
#     def part(self):
#         print(f"this city is {self.TYPE} !")
#
#
# class region(country):
#     TYPE = "Kyiv region"
#
#
#     def city(self):
#         print(f" {self.TYPE} is captal of Ukraine!")
#
#
# class Kyiv(region, country):
#     TYPE = "Kyiv"
#
#
# my_home_kiev = Kyiv()
# my_home_kiev.part()
# my_home_kiev.city()

# Задание 4
# Создайте UML-диаграммы к заданиям 1 и 3. Сохраните их в формате *.um

# задание 1
#
#
#
#
# Задание 5
# Используя код example_10, создайте декораторы @staticmethod для определения совершеннолетия человека в Украине и Америки.

# from datetime import date
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#
#     @staticmethod
#     def country(age, countr):
#         if countr == "ukraine":
#             if age > 18:
#                 print(f"in {countr} you are age")
#             else:
#                 print(f" in {countr}, you aren`t age ")
#         if countr == "USA":
#             if age > 19:
#                 print(f" in the {countr} you are age ")
#             else:
#                 print(f"in the {countr} you aren`t age ")
#
#
# person1 = Person("ukraine", 2)
# person2 = Person.fromBirthYear("USA", 2000)
#
# (person1.age)
# (person2.age)
#
# print(Person.country(4, "USA"))
