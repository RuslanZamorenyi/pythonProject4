# Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.
# def sums():
#     numbers = [2, 4, 3, 15, 12, 22]
#     list_one = filter(lambda x: x % 2, numbers)
#     list_two = map(lambda y: y ** 2, list_one)
#     print(list(list_two))
#
# sums()


# def fib(n):
#     list1 = []
#     a, b = 0, 1
#     for __ in range(n):
#         yield a
#         a, b = b, a + b
# 
#         def decorator(fn):
#             def decorated_fn(*args, **kwargs):
#                 fn(*args, **kwargs)  # виклик початкової функції
#
#             return decorated_fn
#
#         @decorator
#         def better_list():
#             if a % 2:
#                 list1.append(a)
#
#         print(list1)
#
#         better_list()
#
#
# list(fib(10))


