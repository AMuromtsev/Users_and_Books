import json
import csv
from csv import DictReader


with open("./data/books.csv", "r") as file:
    reader_books = DictReader(file)
    list_of_books = list(reader_books)
    # header_books = next(reader_books)

# def gen_func():
#     for k in range(0, len(list_of_books)):
#
#         yield int(list_of_books(k))


with open("./data/users.json", "r") as file:
    users = json.load(file)

i = 0  # счётчик для пользователей

for i in range(i, len(users)):
     for key in list(users[i].keys()):
         if key not in ('name', 'gender', 'address', 'age'):
             del users[i][key]
         users[i]["books"] = []
         users[i]["books"].append(list_of_books[i])                  #сюда нужна функция - генератор, но я не понимаю как её написать
     print(users[i])


with open("./data/reference.json", "w") as f:
    json.dump(users, f, indent=4)
