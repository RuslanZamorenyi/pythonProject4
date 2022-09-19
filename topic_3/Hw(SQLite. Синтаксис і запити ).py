# Завдання 1
# Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час.
# file (table.sql)

# Завдання 2
# Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних.

import sqlite3

try:
    sqlite_connection = sqlite3.connect('table.bd')
    cursor = sqlite_connection.cursor()
    print("База даних підключена до SQLite")

    sqlite_alter_query = """ALTER TABLE table
                          (name)  VALUES  ('Ruslan')"""

    count = cursor.execute(sqlite_alter_query)
    sqlite_connection.commit()
    print("Запис успішно вставлено до таблиці sqlitedb_developers ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Неможливо вставити дані в таблицю sqlite")
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("З'єднання з SQLite закрито")


# Створіть агрегатні функції для підрахунку загальної кількості витрат і витрат за місяць.
# Забезпечте відповідний інтерфейс користувача.


# Завдання 4
# Змініть таблицю так, щоби можна було додати не лише витрати, а й доходи.
# file (table.sql)

