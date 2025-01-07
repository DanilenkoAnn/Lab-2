 #Задание№1
import csv


with open('books.csv') as text:
    reader = csv.reader(text, delimiter=';')  
    for row in reader:
        if len(row[1]) > 30:
            print(row[1])


# #Задание№2
# import csv


# def search_books_by_author(author_name):
#     books = []
    
    
#     with open('books-en.csv') as file:
#         reader = csv.DictReader(file, delimiter=';')  

#         for row in reader:
#             try:
#                 year = int(row['Year-Of-Publication'])   
                
#                 if year >= 2018 and author_name.lower() in row['Book-Author'].lower():
#                     books.append(row)  
#             except ValueError:
#                 continue   

#     return books

 
# author_to_search = input("Введите имя автора для поиска книг: ")
# found_books = search_books_by_author(author_to_search)
 

# if found_books:
#     print(f"\nКниги автора '{author_to_search}' с 2018 года:")
#     for book in found_books:
#         print(f"Название: {book['Title']}, Год: {book['Year']}")
# else:
#     print(f"Нет книг автора '{author_to_search}' с 2018 года.")




# # #Задание№3
# import csv

 
# bibliography = []


# with open('books-en.csv') as text:
#     reader = csv.reader(text, delimiter=';')
#     for row in reader:
#         books = list(reader)   

 
# with open('books-en.csv') as file:
#     reader = csv.reader(file, delimiter=';')  


#     count = 0   
#     for row in reader:
#         if len(row) >= 4:   
#             isbn = row[0]
#             title = row[1]
#             author = row[2]
#             year = row[3]

             
#             citation = f"{author}. \"{title}.\" {year}, ISBN: {isbn}."
#             bibliography.append(citation)
#             count += 1


#             if count >= 21:
#                 break

 
# with open('bibliography.txt', mode='w', encoding='utf-8') as bibliography_file:
#     for entry in bibliography:
#         bibliography_file.write(entry + '\n')


# print("Библиографические ссылки успешно созданы и сохранены в файл bibliography.txt.")


#Задание №4
# import xml.etree.ElementTree as ET

 
# tree = ET.parse('currency.xml')
# root = tree.getroot()

 
# currency_list = []

 
# date_str = root.attrib['Date']
# year = int(date_str.split('.')[2])  

 
# if year >= 2018:

#     for currency in root.findall('Valute'):
#         name = currency.find('Name').text  
#         char_code = currency.find('CharCode').text   
        
#         currency_list.append((name, char_code))
 

# with open('currency_rates.csv', 'w', encoding='utf-8-sig') as f:
     
#     f.write("Name,CharCode\n")
     
#     for name, char_code in currency_list:
#         f.write(f"{name},{char_code}\n")

 
# print("Данные успешно записаны в файл currency_rates.csv")


# #перечень издательств без повторений
# import csv

 
# publishers = set()

 
# with open('books-en.csv') as file:
#     reader = csv.DictReader(file, delimiter=';')  

     
#     for row in reader:
#         if isinstance(row, dict):   
#             publisher = row.get('Publisher')   
#             if publisher:
#                 publishers.add(publisher)

 
# print("Уникальные издательства:")


# for publisher in sorted(publishers):
#     print(publisher)


# #Самые популярные 20 книг
# import csv
# books = []

 
# with open('books-en.csv') as file:
#     reader = csv.DictReader(file, delimiter=';')   
    
 
#     for row in reader:
#         title = row.get('Book-Title')   
#         downloads = row.get('Downloads')   
        
        
#         if title and downloads:
#             try:
#                 downloads = float(row['Downloads']) 
#                 books.append((title, downloads))
#             except ValueError:
#                 continue   

 
# top_books = sorted(books, key=lambda x: x[1], reverse=True)[:20]

 
# print("\n20 самых популярных книг:")
# for title, downloads in top_books:
#     print(f"{title}: {downloads} загрузок")

 
 

 