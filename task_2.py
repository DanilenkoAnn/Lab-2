# #Задание№2
import csv

def search_books_by_author(author_name):
    books = []
    
    with open('books-en.csv') as file:
        reader = csv.DictReader(file, delimiter=';')   

        for row in reader:
            try:
                year = int(row['Year-Of-Publication'])   
                if year >= 2000 and author_name.lower() in row['Book-Author'].lower():
                    books.append(row)   
            except ValueError:
                continue   
    return books


author_to_search = input("Введите имя автора для поиска книг: ")
found_books = search_books_by_author(author_to_search)


if found_books:
    print(f"\nКниги автора '{author_to_search}' с 2000 года:")
    for book in found_books:
        print(f"Название: {book['Book-Title']}, Год: {book['Year-Of-Publication']}")
else:
    print(f"Нет книг автора '{author_to_search}' с 2000 года.")