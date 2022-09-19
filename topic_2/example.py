
def fib(n):
    list1 = []
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b
    #     if a % 2:
    #         list1.append(a)
    # print(list1)


 def decorator(fn):
            def decorated_fn(*args, **kwargs):

                fn(*args, **kwargs)  # виклик початкової функції

            return decorated_fn



        @decorator
        def better_list():
            if a % 2:
                list1.append(a)
        print(list1)

        better_list()


list(fib(10))

# def cast_result(type_):
#     """Приклад створення декоратора з параметром"""
#
#     def cast_decorator(function):
#         """Сам декоратор"""
#
#         def decorated_function(*args, **kwargs):
#             result = function(*args, **kwargs)
#             return type_(result)
#
#         return decorated_function
#
#     return cast_decorator
#
#
# @cast_result(float)
# def add(x, y):
#     return x + y
#
#
# print(add(2, 3))
#
#
# import decimal
#
#
# @cast_result(repr)
# @cast_result(decimal.Decimal)
# def div(x, y):
#     return x / y
#
#
# print(div(3, 2))
# print(type(div(3, 2)))


import csv
quoting = csv.QUOTE_ALL

with open('file_2.csv', 'w') as f:

    writer = csv.DictWriter(
        f,
        fieldnames=['name', 'region', 'age'],
        quoting=quoting
    )

    writer.writeheader()

    writer.writerow({
        'name': 'Ruslan',
        'region': 'Kiev',
        'age': 20
    })
    writer.writerow({
        "name": "Maks",
        "region": "Dnipro",
        "age": 20
    })