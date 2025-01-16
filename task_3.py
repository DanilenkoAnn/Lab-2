# #Задание№3
import csv

 
bibliography = []


with open('books-en.csv') as text:
    reader = csv.reader(text, delimiter=';')
    for row in reader:
        books = list(reader)   

 
with open('books-en.csv') as file:
    reader = csv.reader(file, delimiter=';')  


    count = 0   
    for row in reader:
        if len(row) >= 4:   
            isbn = row[0]
            title = row[1]
            author = row[2]
            year = row[3]

             
            citation = f"{author}. \"{title}.\" {year}, ISBN: {isbn}."
            bibliography.append(citation)
            count += 1


            if count >= 21:
                break

 
with open('bibliography.txt', mode='w', encoding='utf-8') as bibliography_file:
    for entry in bibliography:
        bibliography_file.write(entry + '\n')


print("Библиографические ссылки успешно созданы и сохранены в файл bibliography.txt.")