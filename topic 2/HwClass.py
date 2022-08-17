# Завдання 1
# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього операції перевірки на рівність та нерівність, методи _repr_ та _str_.\
# class Describe_book:
#     def __init__(self, name, author, year, genre):
#         self.name = name
#         self.author = author
#         self.year = year
#         self.genre = genre
#
#
#     def describe(self):
#         print("Name book {}, author is {}, {} year, genre is {}.". format(self.name, self.author, self.year, self.genre))
#
# book1 = Describe_book("Alchemist", "Пауло Коэльо", 1988, "novel")
# book2 = Describe_book("Идиот", "Фёдор Достоевский", 1868, "novel")
# book3 = Describe_book("Harry Potter", "Джоан Роулинг", "first book 1997", "novel, fantasy")
#
# books = [book1, book2, book3]
# for describe_book in books:
#     describe_book.describe()


# Завдання 2
# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.


# class Describe_book:
#     def __init__(self, name, author, year, genre, response):
#         self.name = name
#         self.author = author
#         self.year = year
#         self.genre = genre
#         self.response = response
#
#
#     def describe(self):
#         print("Name book {}, author is {}, {} year, genre is {}, response to book: {}.".
#               format(self.name, self.author, self.year, self.genre, self.response))
#
# book1 = Describe_book("Alchemist", "Пауло Коэльо", 1988, "novel", "\n\t1.Интересная и поучительная притча \n\t2.Не всем "
#                                                                   "может понравиться, впрочем, так и с каждой книгой.")
# book2 = Describe_book("Идиот", "Фёдор Достоевский", 1868, "novel", "\n\t1.Классика, произведение с глубоким смыслом "
#                                                                    "\n\t2.Нелегко читать, трудно осмыслить")
# book3 = Describe_book("Harry Potter", "Джоан Роулинг", "first book 1997",
#                       "novel, fantasy", "\n\t1.Намного интереснее фильма, интересные истории\n\t2.Слишком много смертей")
#
# books = [book1, book2, book3]
# for describe_book in books:
#     describe_book.describe()

