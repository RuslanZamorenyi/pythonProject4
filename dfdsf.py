# class Rectangle:
#
#     def __init__(self, name):
#         self.name = name
#
#     def fun(self):
#         print("{}".format(self.name))
#
# class Button:
#     def __init__(self, button):
#         self.button = button
#
#
#     def fun(self):
#         print("{}".format(self.button))
#
# button.fun()





# from datetime import date


# class MyClass1:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, surname, name, birthYear):
#         print(self.surname + self.name + "'s age is: " + str(self.age))
#         return cls(surname, name, date.today().year - birthYear)
#
#     def print_info(self):
#         if self.age < 18:
#             print(self.surname + self.name + "'s age is: " + str(self.age) + "тож він не понолітній")
#         # elif self.age < 19:
#         #     print(self.surname + self.name + "'s age is: " + str(self.age) + "тож він не понолітній")
#
#         else:
#             print(self.surname + self.name + "'s age is: " + str(self.age) + "тож він понолітній")


# class MyClass2(MyClass1):
#     color = 'White'

#
# m_per1 = MyClass1('Ivanenko', 'Ivan', 1)
# m_per1.print_info()
# #
# m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000)
# m_per2.print_info()
# #
# m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
# print(isinstance(m_per3, MyClass2))
#
# m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
# print(isinstance(m_per4, MyClass1))
#
# print(issubclass(MyClass1, MyClass2))
# print(issubclass(MyClass2, MyClass1))





# from datetime import date
#
#
# class MyClass1:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, surname, name, birthYear):
#         return cls(surname, name, date.today().year - birthYear)
#
#     def print_info(self):
#         if self.age > 18:
#             print(self.surname + self.name + "'s age is: " + str(self.age) + "тож він повнолітній в укрїні")
#         # else:
#         #     print(self.surname + self.name + "'s age is: " + str(self.age) + "тож він не повнолітній в укрїні")
#
#
# m_per1 = MyClass1('Ivanenko', 'Ivan', 1)
# m_per1.print_info()
#
# m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2000 )
# m_per2.print_info()



# class Car:
#
#
#
#     def __init__(self, colour, brand, year):
#         self.colour = colour
#         self.brand = brand
#         self.year = year
#
#     def _get (self):
#         print(f"this car has {self.colour} colour, it brand is {self.brand}, it is {self.year} year")
#
#     def _set(self, field, new_value):
#         self._field = new_value
#         if field == 'colour':
#             self.colour = new_value
#         elif field == 'brand':
#             self.brand = new_value
#         elif field == 'colour':
#             self.year = new_value
#
#
# car = Car("blue", "BMW", 2022)
# car._get()
# car._set('colour', "red")
# car._get()


# class Outer:
#     """Outer Class"""
#
#     def __init__(self):
#         ## Instantiating the 'Inner' class
#         self.inner = self.Inner()
#         ## Instantiating the '_Inner' class
#         self._inner = self._Inner()
#
#     def show_classes(self):
#         print("This is Outer class")
#         print(inner)
#         print(_inner)
#
#     class Inner:
#         """First Inner Class"""
#
#         def inner_display(self, msg):
#             print("This is Inner class")
#             print(msg)
#
#     class _Inner:
#         """Second Inner Class"""
#
#         def inner_display(self, msg):
#             print("This is _Inner class")
#             print(msg)
a = input("djdsdkdkf")

if a == "піднесення до ступеня":
    w = float(input("введіть число:"))
    while True:
        # w = float(input("введіть число:"))
        v = float(input("введіть ступінь:"))
        if w == 0:
            try:
                v > 0
                print(w ** v)
                break
            except:
                print("помилка! ступінь не може буді відєина ")
        else:
            print(w ** v)
            break


    # while True:
    #     v = float(input("введіть ступінь:"))
    #     try:
    #         v != 0
    #         print(w ** v)
    #         break
    #     except:
    #         print("помилка! ступінь не може буді відєина ")
    # # print(d / e)

