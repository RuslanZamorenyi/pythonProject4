# Завдання 1
# Створіть співпрограму, яка отримує контент із зазначених посилань і логує хід виконання в спеціальний файл,
# використовуючи стандартну бібліотеку urllib, а потім проробіть те саме з бібліотекою aiohttp. Кроки, які мають
# бути залоговані: початок запиту до адреси X, відповідь для адреси X отримано зі статусом 200. Перевірте хід виконання
# програми на > 3 ресурсах і перегляньте послідовність запису логів в обох варіантах і порівняйте результати.
# Для двох видів завдань використовуйте різні файли для логування, щоби порівняти отриманий результат.
import urllib
from datetime import datetime

import aiohttp
import asyncio

resources = [
    'https://jsonplaceholder.typicode.com/todos/1',
    'http://example.com',
]

async def main():
    async with aiohttp.ClientSession() as session:
        for i in resources:
            time_start = datetime.now()
            async with session.get(i) as response:

                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                html = await response.text()
                print("Body:", html[:15], "...")
            time_end = datetime.now()
            with open("Example2.0", "a") as f1:
                dict_fgl = {
                    "time_start": time_start,
                    "time_end": time_end,
                    "response": response,
                }
                f1.write(str(dict_fgl))
def urllib_workers():
    for res in resources:
        time_start = datetime.now()
        req = urllib.request.Request(res)
        time_end = datetime.now()

        with open("Example2.1", "a") as f1:
            dict_fgl = {
                "time_start": time_start,
                "time_end": time_end,
                "response": req
            }
            f1.write(str(dict_fgl))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
urllib_workers()