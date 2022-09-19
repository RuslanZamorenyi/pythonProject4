# 1.
# Извлечь телефоны с сайта «https://www.miraton.ua/». Данные сохранить в текстовый файл.

# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://www.miraton.ua/"
# page = requests.get(URL)
#
# soup = BeautifulSoup(page.content, "html.parser")
#
#
# job_elements = soup.find_all("li", class_="footer-contacts-col")
#
# list_phone = []
# for i in job_elements:
#     for el in i("li"):
#         list_phone.append(el.text)
#     break
#
# print(list_phone)

# 2.
# Извлечь все контактные данные (телефоны, почта, соцсети и т.д.) с сайта «https://eldorado.ua/uk/».
# Данные сохранить в текстовый файл.

# import requests
# from bs4 import BeautifulSoup
# URL = "https://eldorado.ua/uk/"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")
# job_elements = soup.find_all("a", class_="tel")
#
# list_phone = []
# for i in job_elements:
#     list_phone.append(i.text)
#
# second_element = soup.find_all("div", class_="1/5--desktop-large 1/5--desktop-small 1/5--tablet 4/4--mobile grid__cell cards-list applications")
# link_element = []
#
# for i in second_element:
#     links = i.find_all("a")
#     for link in links:
#         link_element.append(link["href"])
#
# contact_dict = {'phones': list_phone, 'social_media': link_element}
#
#
# with open("file.txt", "a") as f1:
#     f1.write(f'{contact_dict} \n')
