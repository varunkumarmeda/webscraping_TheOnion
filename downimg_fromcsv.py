import csv 
import requests 
 
with open('theonion.csv') as csvfile: 
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"') 
    for row in csvrows: 
        filename = row[0] 
        url = row[2] 
        print(url) 
        result = requests.get(url, stream=True) 
        if result.status_code == 200: 
            image = result.raw.read() 
            open(filename + ".png","wb").write(image) 