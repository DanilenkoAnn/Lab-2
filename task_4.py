#Задание №4
import xml.etree.ElementTree as ET

 
tree = ET.parse('currency.xml')
root = tree.getroot()

 
currency_list = []

 
date_str = root.attrib['Date']
year = int(date_str.split('.')[2])  

 
if year >= 2018:

    for currency in root.findall('Valute'):
        name = currency.find('Name').text  
        char_code = currency.find('CharCode').text   
        
        currency_list.append((name, char_code))
 

with open('currency_rates.csv', 'w', encoding='utf-8-sig') as f:
     
    f.write("Name,CharCode\n")
     
    for name, char_code in currency_list:
        f.write(f"{name},{char_code}\n")

 
print("Данные успешно записаны в файл currency_rates.csv")


 