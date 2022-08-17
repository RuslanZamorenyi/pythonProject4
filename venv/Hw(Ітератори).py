# Завдання 1
# Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable

# iterable_objects = [1, 2, 3, 4, 5, 6]
#
# my_objects = iter(iterable_objects)
#
# print(next(my_objects))
#
# print(my_objects.__next__())
# print(my_objects.__next__())
# print(my_objects.__next__())
#
# next(my_objects)


# iterable_objects = [1, 2, "c", "one", "hot"]
#
# my_objects = iter(iterable_objects)
# # print(next(my_objects))
# while True:
#     try:
#         object = next(my_objects)
#         print(object)
#
#     except StopIteration:
#         break


# Завдання 2
# Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, додавши методи очищення списку,
# додавання елемента у довільне місце списку, видалення елемента з кінця та довільного місця списку.



# class MyList(object):
#     """Клас списку"""
#
#     class _ListNode(object):
#         """Внутрішній клас списку"""
#
#         # За умовчанням атрибути-дані зберігаються у словнику __dict__.
#         # Якщо можливість динамічно додавати нові атрибути
#         # не потрібно, можна заздалегідь їх описати, що більше
#         # ефективно з точки зору пам'яті та швидкодії, що
#         # особливо важливо, коли створюється безліч екземлярів
#         # даного класу.
#         __slots__ = ('value', 'prev', 'next')
#
#         def __init__(self, value, prev=None, next=None):
#             self.value = value
#             self.prev = prev
#             self.next = next
#
#         def __repr__(self):
#             return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))
#
#     class _Iterator(object):
#         """Внутрішній клас ітератора"""
#
#         def __init__(self, list_instance):
#             self._list_instance = list_instance
#             self._next_node = list_instance._head
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self._next_node is None:
#                 raise StopIteration
#
#             value = self._next_node.value
#             self._next_node = self._next_node.next
#
#             return value
#
#     def __init__(self, iterable=None):
#         # Довжина списку
#         self._length = 0
#         # Перший елемент списку
#         self._head = None
#         # Останній елемент списку
#         self._tail = None
#
#         # Додавання всіх переданих елементів
#         if iterable is not None:
#             for element in iterable:
#                 self.append(element)
#
#     def append(self, element):
#         """Додавання елемента до кінця списку"""
#
#         # Створення списку
#         node = MyList._ListNode(element)
#
#         if self._tail is None:
#             # Список поки що порожній
#             self._head = self._tail = node
#         else:
#             # Додавання елемента
#             self._tail.next = node
#             node.prev = self._tail
#             self._tail = node
#
#         self._length += 1
#
#     def __len__(self):
#         return self._length
#
#     def list_insert(self, element, index):
#         node = MyList._ListNode(element, index)
#
#         if self._tail is None:
#             self._head = self._tail = node
#         else:
#             node.insert(element, index)
#
#     def list_pop(self, index):
#         if self._tail is None:
#             self._head = self._tail = node
#         else:
#             node.pop([index])
#
#
#     def list_clear(self):
#             node = MyList._ListNode()
#             node.clear()
#
#     def __repr__(self):
#         # Метод join класу str приймає послідовність рядків
#         # і повертає рядок, у якому всі елементи цієї
#         # Послідовності з'єднані початковим рядком.
#         # Функція map застосовує задану функцію всім елементам послідовності.
#         return 'MyList([{}])'.format(', '.join(map(repr, self)))
#
#     def __getitem__(self, index):
#         if not 0 <= index < len(self):
#             raise IndexError('list index out of range')
#
#         node = self._head
#         for _ in range(index):
#             node = node.next
#
#         return node.value
#
#     def __iter__(self):
#         return MyList._Iterator(self)
#
#
# def main():
#     # Створення списку
#     my_list = MyList([1, 2, 5])
#
#     # Виведення довжини списку
#     print(len(my_list))
#
#     # Відображення самого списку
#     print(my_list)
#
#     print()
#
#     # Обхід списку
#     for element in my_list:
#         print(element)
#
#     print()
#
#     # Повторний обхід списку
#     for element in my_list:
#         print(element)
#
#
# if __name__ == '__main__':
#     main()



