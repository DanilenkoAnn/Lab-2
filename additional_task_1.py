#перечень издательств без повторений
import csv

 
publishers = set()

 
with open('books-en.csv') as file:
    reader = csv.DictReader(file, delimiter=';')  

     
    for row in reader:
        if isinstance(row, dict):   
            publisher = row.get('Publisher')   
            if publisher:
                publishers.add(publisher)

 
print("Уникальные издательства:")


for publisher in sorted(publishers):
    print(publisher)