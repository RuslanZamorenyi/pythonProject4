# Завдання 1
# Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу.

# import json
#
# data = {
#     "first name ": "Ruslan",
#     "age": "20",
#     "learing": "NAU",
#     "from": "Kiev"
#
# }
# json_data = json.dumps(data)
# print(json_data)
#
# with open("file_1.json", "w") as f:
#     json.dump(data, f)
#
# import json
#
# with open("file_1.json", "r") as f:
#     data = json.load(f)
#     print(data)

# Завдання 1
# Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу.


# import xml.etree.cElementTree as ET
#
# tree = ET.parse('example_1.xml')
# tree.findall("Books/Book")
#
# tree.find("Books/Book[Title='The Colour of Magic']")

# tree.find("Books/Book[@id='5']")

# tree.find("Books/Book[2]")

# tree.find("Books/Book[last()]")

# tree.findall(".//Author")
#
# for book in tree.find("Books/Book[Title='The Colour of Magic']"):
#     print(book.text)


# Попрацюйте зі створенням власних діалектів, довільно вибираючи правила для CSV-файлів. Зареєструйте створені діалекти
# та попрацюйте, використовуючи їх зі створенням файлом.


# import csv
#
#
# class CustomDialect(csv.Dialect):
#
#     quoting = csv.QUOTE_ALL
#
#     quotechar = "-"
# 
#     delimiter = "-"
#     lineterminator = '\n'
#
#
#
# csv.register_dialect('tester', CustomDialect)
#
# with open('file_2.csv', 'w') as f:
#     writer = csv.writer(f, dialect='tester')
#     writer.writerow(['I', 'look', 'like'])
#     writer.writerow(['You', 'very', 'strange'])
