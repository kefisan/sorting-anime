import time
import csv

import sorting_algorithms as sa

sa.column = 8

def sort_and_write(sort_function, data, output_file):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    print(f"Time taken to perform the {sort_function.__name__} is: {end_time - start_time} seconds")

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow([row[1], row[sa.column]])


def process_data(num_rows, file_prefix):
    with open('Anime.csv', 'r') as f:
        reader = csv.reader(f)
        anime_data = [next(reader) for _ in range(num_rows)]
    anime_data = anime_data[1:]
    anime_data = [row for row in anime_data if row[sa.column] != '']

    data = [list(row) for row in anime_data]

    sort_and_write(sa.insertion_sort, data, f'output_rating/{file_prefix}anime_rating_insertion_sort.csv')
    sort_and_write(sa.quick_sort, data, f'output_rating/{file_prefix}anime_rating_quick_sort.csv')
    sort_and_write(sa.heap_sort, data, f'output_rating/{file_prefix}anime_rating_heap_sort.csv')
    sort_and_write(sa.radix_sort, data, f'output_rating/{file_prefix}anime_rating_radix_sort.csv')


for i in range(100, 2100, 100):
    process_data(i, f"{i}_")

for i in range(4000, 19000, 1000):
    process_data(i, f"{i}_")