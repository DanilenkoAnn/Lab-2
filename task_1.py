#Задание№1
import csv


with open('books.csv') as text:
    reader = csv.reader(text, delimiter=';')  
    count = 0
    for row in reader:
        if len(row[1]) > 30:
            count += 1
    print(count)