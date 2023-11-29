# This code generates the data according to the task.
# However, algorithms were also tested on original dataset.
# To perform original data test one may simply change the name of original_sorting_algorithms.py
# to sorting_algorithms.py and original_Anime.csv to Anime.csv

import csv
import random

with open('original_Anime.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[1:]

for row in data:
    row[8] = random.randint(1000, 9999)
    row[9] = random.randint(1901, 2023)

data.sort(key=lambda x: x[8])

with open('Anime.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)