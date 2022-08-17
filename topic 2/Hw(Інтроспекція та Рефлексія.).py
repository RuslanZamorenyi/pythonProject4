# 1.
# Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact, sent_message.
# Створити клас UpdateContact з полями surname, name, age, mob_phone, email, job. Додати методи get_message. Використати
# можливість роботи с атрибутами __dict__, __base__, __bases__. Роздрукувати інформацію на екрані.

class Contact:

    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        print(f"surname employee is {self.surname} name {self.name}, age is {self.age}, number phone:{self.mob_phone}"
              f" and gmail:{self.email}")

    def sent_message(self):
        pass



class UpdateContact():
    def __init__(self, surname, name, age, mob_phone, email, job ):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email
        self.job = job

    def get_contact(self):
        print(f"surname employee is {self.surname} name {self.name}, age is {self.age}, number phone:{self.mob_phone}"
              f" and gmail:{self.email} job is {self.job} ")

emp1 = Contact("Melon", "mark", 18, 45664445445, "rzamorenyj@gmail.com")
emp2 = UpdateContact("Melon", "mark", 18, 45664445445, "rzamorenyj@gmail.com", "boss")
emp1.get_contact()
emp2.get_contact()
print(Contact.__dict__, "\n", Contact.__base__, Contact.__bases__)
print(UpdateContact.__dict__, "\n", UpdateContact.__base__, UpdateContact.__bases__)

# 2
# Використовуючи код з завдання 2, використати функції hassttr(), getattr(), setattr(), delattr().

# getattr()


class_name = "Contact"
method = "get_contact"
emp1 = globals()[class_name](1, 2, 3, 4, 5)
print(getattr(emp1, method)())
print("name = ", getattr(emp1, "name"))

class_name = "UpdateContact"
method = "get_contact"
emp2 = globals()[class_name](5, 6, 7, 8, 9, 10)
print(getattr(emp2, method)())
print("surname = ", getattr(emp2, "surname"))

# hasattr()


print(hasattr(emp1, "age"))
print(hasattr(emp1, "job"))

print(hasattr(emp2, "email"))
print(hasattr(emp2, "hobby"))

# delattr()


delattr(emp1, "age", )
# x = getattr(emp1, "age")
# print(x)
y = getattr(emp1, "age", 18)
print(y)

delattr(emp2, "job")
# b = getattr(emp2, "job")
# print(b)
g = getattr(emp2, "job", "empty")
print(g)

# setattr()


setattr(emp1, "name", "john")
print(emp1.name)

setattr(emp2, "mob_phone", "000000")
print(emp2.mob_phone)

# 3.
# Використовуючи код з завдання 2, створити 2 єкземпляра обох класів. Використати функції isinstance() та issubclass()
# для перевірки єкземплярів.

# isinstance()


print(isinstance(emp1.name, str))
print(isinstance(emp1.name, int))

print(isinstance(emp2.age, int))
print(isinstance(emp2.age, str))

# issubclass()

print(issubclass(Contact, UpdateContact))
print(issubclass(UpdateContact, Contact))




