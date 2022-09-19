# Завдання 1
# Створіть функцію, яка приймає список з елементів типу int, а повертає новий список з рядкових значень вихідного масиву.
# Додайте анотацію типів для вхідних і вислідних значень функції.
# one_list = [4, 12, 23, 45, 16, 25]
# two_list = []
#
#
# def create_new_list(one_list: int) -> str:
#     two_list = []
#
#     for i in one_list:
#         a = str(i)
#         two_list.append(a)
#     print(two_list)
#     return two_list
#
#
# create_new_list(one_list)

# Завдання 2
# Створіть два класи Directory (тека) і File (файл) з типами (анотацією). Клас Directory має мати такі поля:
# • назва (name типу str);
# • батьківська тека (root типу Directory);
# • список файлів (список типу files, який складається з екземплярів File);
# • список підтек (список типу sub_directories, який складається з екземплярів Directory).
# Клас Directory має мати такі поля:
# • додавання теки до списку підтек (add_sub_directory, який приймає екземпляр Directory та присвоює поле root
# для приймального екземпляра);
# • видалення теки зі списку підтек (remove_sub_directory, який приймає екземпляр Directory та обнуляє поле root.
# Метод також видаляє теку зі списку sub_directories);
# • додавання файлу в теку (add_file, який приймає екземпляр File і присвоює йому поле directory – див. клас File нижче);
# • видалення файлу з теки (remove_file, який приймає екземпляр File та обнуляє у нього поле directory.
# Метод видаляє файл зі списку files)
# Клас File має мати такі поля:
# • назва (name типу str);
# • тека (Directory типу Directory)

class Directory:
    def __init__(self, name: str, list_root, list_files, sub_directories ):
        self.name = name
        self.list_root = []
        self.list_files = []
        self.sub_directories = sub_directories

    def add_sub_directory(self, root: str):
        self.root = root
        self.list_root.append(self.root)

    def remove_sub_directory(self):
        del
    def add_file(self):
        d
    def remove_file(self):
        g

class File(Directory):

    def name():
        d
    def directory():
        g



