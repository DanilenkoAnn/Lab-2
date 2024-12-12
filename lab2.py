#  #Задание№1
# import csv


# with open('books.csv') as text:
#     reader = csv.reader(text, delimiter=';')  
#     for row in reader:
#         if len(row[1]) > 30:
#             print(row[1])


# #Задание№2
# # Поиск книг по автору
# author_to_search = input("Введите имя автора для поиска: ")
# limit = 5  # Устоновите лимит по своему выбору
# matching_books = []

# with open('books.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if author_to_search.lower() in row['Автор'].lower():
#             matching_books.append(row)

# # Выводим только ограниченное количество результатов
# for i, book in enumerate(matching_books[:limit], start=1):
#     print(f"{i}. Название: {book['Название']}, Автор: {book['Автор']}, Год: {book['Год']}")


#Задание№3
import random
import csv

 
generator = []


with open('books-en.csv') as text:
    reader = csv.reader(text, delimiter=';')
    for row in reader:
        books = list(reader)   


random_books = random.sample(books, 20)


for book in random_books:
    title = book[1]
    author = book[2]
    year = book[3]
    generator.append(f"{author}. {title} - {year}")


with open('generator.txt', 'w') as text:
    for i, books in enumerate(generator, start=1):
        text.write(f"{i}. {books}\n")


 


 