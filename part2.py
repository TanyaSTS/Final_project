import requests
import json

base_url = "https://www.labirint.ru/"
#1 Тест API главной страницы
r = requests.get(base_url)
test_status = r.status_code == 200
print (test_status)
texts = r.content
print(type(texts))

#2 Test API of the "books" page
r = requests.get(base_url + "books/")
test_status = r.status_code == 200
print (test_status)
texts = r.content

#3 Test API of the "best" page
r = requests.get(base_url + "best/")
test_status = r.status_code == 200
print (test_status)
texts = r.content

#4 Test API of the "school" page
r = requests.get(base_url + "school/")
test_status = r.status_code == 200
print (test_status)
texts = r.content

#5 Test API of the "games" page
r = requests.get(base_url + "games/")
test_status = r.status_code == 200
print (test_status)
texts = r.content

#6 Test API of the "office" page
r = requests.get(base_url + "office/")
test_status = r.status_code == 200
print (test_status)
texts = r.content

#7 Test API of the "club" page
r = requests.get(base_url + "club/")
test_status = r.status_code == 200
print (test_status)
texts = r.content

#8 Test API of the "cabinet" page
r = requests.get(base_url + "cabinet/")
test_status = r.status_code == 200
print (test_status)
texts = r.content

#9 Test API of the "putorder" page
r = requests.get(base_url + "cabinet/putorder/")
test_status = r.status_code == 200
print (test_status)
texts = r.content


#10 Test API of the "cart" page
r = requests.get(base_url + "cart/")
test_status = r.status_code == 200
print (test_status)
texts = r.content




url = "https://www.labirint.ru/"
