import time
import csv


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and float(data[j][8]) > float(key[8]):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i][8] < pivot[8]:
            i += 1
        j -= 1
        while arr[j][8] > pivot[8]:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)
    return arr

def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and float(data[i][8]) < float(data[left][8]):
        largest = left

    if right < n and float(data[largest][8]) < float(data[right][8]):
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)


def heap_sort(data):
    n = len(data)

    for i in range(n, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)


def counting_sort(data, exp1):
    n = len(data)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (int(float(data[i][8]) * 100) // exp1)
        count[(index) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (int(float(data[i][8]) * 100) // exp1)
        output[count[(index) % 10] - 1] = data[i]
        count[(index) % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(data)):
        data[i] = output[i]


def radix_sort(data):
    max1 = max(float(row[8]) * 100 for row in data)
    exp = 1
    while max1 // exp > 0:
        counting_sort(data, exp)
        exp *= 10



with open('Anime.csv', 'r') as f:
    reader = csv.reader(f)
    anime_data = list(reader)

anime_data = anime_data[1:]
anime_data = [row for row in anime_data if row[8] != '']

data_insertion_sorted = [list(row) for row in anime_data]
start_time = time.time()
insertion_sort(data_insertion_sorted)
end_time = time.time()
print("Time taken to perform the insert sort is: %s seconds" % (end_time - start_time))

with open('insertion_sort.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data_insertion_sorted:
        row_to_write = list(row)  # create a copy of the row
        # row_to_write[1] = row_to_write[1] + " (" + row_to_write[8] + ")"
        writer.writerow([row_to_write[1], row_to_write[8]])

data_quick_sorted = [list(row) for row in anime_data]
start_time = time.time()
quick_sort(data_quick_sorted)
end_time = time.time()
print("Time taken to perform the quick sort is: %s seconds" % (end_time - start_time))

with open('quick_sort.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data_quick_sorted:
        row_to_write = list(row)  # create a copy of the row
        # row_to_write[1] = row_to_write[1] + " (" + row_to_write[8] + ")"
        writer.writerow([row_to_write[1], row_to_write[8]])

# For heapsort
data_heap_sorted = [list(row) for row in anime_data]
start_time = time.time()
heap_sort(data_heap_sorted)
end_time = time.time()
print("Time taken to perform the heap sort is: %s seconds" % (end_time - start_time))

with open('heap_sort.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data_heap_sorted:
        row_to_write = list(row)  # create a copy of the row
        # row_to_write[1] = row_to_write[1] + " (" + row_to_write[8] + ")"
        writer.writerow([row_to_write[1], row_to_write[8]])

# For radixsort
data_radix_sorted = [list(row) for row in anime_data]
start_time = time.time()
radix_sort(data_radix_sorted)
end_time = time.time()
print("Time taken to perform the radix sort is: %s seconds" % (end_time - start_time))

with open('radix_sort.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data_radix_sorted:
        row_to_write = list(row)  # create a copy of the row
        # row_to_write[1] = row_to_write[1] + " (" + row_to_write[8] + ")"
        writer.writerow([row_to_write[1], row_to_write[8]])

# for row in data:
#     row[1] = row[1] + " (" + row[8] + ")"
#
# for row in data:
#     print(row[1], row[8])
