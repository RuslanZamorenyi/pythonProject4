# Завдання 1
# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

class Car:



    def __init__(self, colour, brand, year):
        self.colour = colour
        self.brand = brand
        self.year = year

    def _get (self):
        print(f"this car has {self.colour} colour, it brand is {self.brand}, it is {self.year} year")

    def _set(self, field, new_value):
        self._field = new_value
        if field == 'colour':
            self.colour = new_value
        elif field == 'brand':
            self.brand = new_value
        elif field == 'colour':
            self.year = new_value


car = Car("blue", "BMW", 2022)
car._get()
car._set('colour', "red")
car._get()

# Завдання 2
# Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting().
# Обидва створюють різні привітання. Створіть два відповідні обєкти з двох класів вище та викличте дії цих двох обєктів
# в одній функції (функція hello_friend).


# class English:
#     def __init__(self, hello = "Hello!"):
#         self.hello = hello
#
#     def greeting(self):
#         print(self.hello)
# eng = English()
# # eng.greeting()
#
#
# class Spanish:
#     def __init__(self, hello = "Hola!"):
#         self.hello = hello
#
#     def greeting(self):
#         print(self.hello)
# spa = Spanish()
# # spa.greeting()
#
#
# def hello_friend():
#     eng.greeting()
#     spa.greeting()
#
# hello_friend()
