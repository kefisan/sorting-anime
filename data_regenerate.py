import csv
import random

with open('original_Anime.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[1:]

for row in data:
    row[8] = random.randint(1000, 9999)
    row[9] = random.randint(1000, 9999)

data.sort(key=lambda x: x[8])

with open('Anime.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)