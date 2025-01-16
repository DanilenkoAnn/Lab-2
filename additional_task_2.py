#Самые популярные 20 книг
import csv
books = []

 
with open('books-en.csv') as file:
    reader = csv.DictReader(file, delimiter=';')   
    
 
    for row in reader:
        title = row.get('Book-Title')   
        downloads = row.get('Downloads')   
        
        
        if title and downloads:
            try:
                downloads = float(row['Downloads']) 
                books.append((title, downloads))
            except ValueError:
                continue   

 
top_books = sorted(books, key=lambda x: x[1], reverse=True)[:20]

 
print("\n20 самых популярных книг:")
for title, downloads in top_books:
    print(f"{title}: {downloads} загрузок")
