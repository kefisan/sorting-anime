import csv
import time
import random
import matplotlib.pyplot as plt

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and float(data[j][8]) > float(key[8]):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def partition(data, low, high):
    pivot_index = random.randint(low, high)
    data[low], data[pivot_index] = data[pivot_index], data[low]
    pivot = data[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while data[i][8] < pivot[8]:
            i += 1
        j -= 1
        while data[j][8] > pivot[8]:
            j -= 1
        if i >= j:
            return j
        data[i], data[j] = data[j], data[i]


def quick_sort(data, low=0, high=None):
    if high is None:
        high = len(data) - 1
    if low < high:
        pi = partition(data, low, high)
        quick_sort(data, low, pi)
        quick_sort(data, pi + 1, high)
    return data


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
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (int(float(data[i][8]) * 100) // exp1)
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (int(float(data[i][8]) * 100) // exp1)
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
    data[:] = output[:]


def radix_sort(data):
    max1 = max(float(row[8]) * 100 for row in data)
    exp = 1
    while max1 // exp > 0:
        counting_sort(data, exp)
        exp *= 10


def sort_and_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

def plot_sort_times(sort_times):
    for sort_name, times in sort_times.items():
        plt.plot(['18k', '1k', '100'], times, label=sort_name)
    plt.xlabel('Data Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Time Comparison')
    plt.legend()
    plt.show()


sort_functions = [insertion_sort, quick_sort, heap_sort, radix_sort]
sort_names = ['Insertion Sort', 'Quick Sort', 'Heap Sort', 'Radix Sort']

data_sizes = [18000, 1000, 100]
sort_times = {name: [] for name in sort_names}

for data_size in data_sizes:
    with open('Anime.csv', 'r') as f:
        reader = csv.reader(f)
        anime_data = [next(reader) for _ in range(data_size)]

    anime_data = anime_data[1:]
    anime_data = [row for row in anime_data if row[8] != '']

    for sort_function, sort_name in zip(sort_functions, sort_names):
        data_sorted = [list(row) for row in anime_data]
        sort_time = sort_and_time(sort_function, data_sorted)
        print(f"Time taken to perform the {sort_name} on {data_size} lines is: {sort_time} seconds")
        sort_times[sort_name].append(sort_time)

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Plotting the line graph for all data sizes on the first subplot
for sort_name in sort_names:
    axs[0, 0].plot(data_sizes, sort_times[sort_name], marker='o', label=sort_name)
axs[0, 0].set_xlabel('Data Size')
axs[0, 0].set_ylabel('Time (seconds)')
axs[0, 0].set_title('Time taken by sorting algorithms')
axs[0, 0].legend()

# Plotting the bar graphs for each data size on the remaining subplots
bar_width = 0.2
opacity = 0.8

for i, data_size in enumerate(data_sizes):
    for j, sort_name in enumerate(sort_names):
        axs[(i+1) // 2, (i+1) % 2].bar(j + bar_width, sort_times[sort_name][i], bar_width, alpha=opacity, label=sort_name)
    axs[(i+1) // 2, (i+1) % 2].set_xlabel('Sorting Algorithm')
    axs[(i+1) // 2, (i+1) % 2].set_ylabel('Time (seconds)')
    axs[(i+1) // 2, (i+1) % 2].set_title(f'Time taken by sorting algorithms for data size {data_size}')
    axs[(i+1) // 2, (i+1) % 2].set_xticks([r + bar_width for r in range(len(sort_names))])
    axs[(i+1) // 2, (i+1) % 2].set_xticklabels(sort_names)
    axs[(i+1) // 2, (i+1) % 2].legend()

plt.tight_layout()
plt.show()
