import csv
import time
import matplotlib.pyplot as plt

import sorting_algorithms as sa

sa.column = 9


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


sort_functions = [sa.insertion_sort, sa.quick_sort, sa.heap_sort, sa.radix_sort]
sort_names = ['Insertion Sort', 'Quick Sort', 'Heap Sort', 'Radix Sort']

data_sizes = [18000, 1000, 100]
sort_times = {name: [] for name in sort_names}

for data_size in data_sizes:
    with open('Anime.csv', 'r') as f:
        reader = csv.reader(f)
        anime_data = [next(reader) for _ in range(data_size)]

    anime_data = anime_data[1:]
    anime_data = [row for row in anime_data if row[sa.column] != '']

    for sort_function, sort_name in zip(sort_functions, sort_names):
        data_sorted = [list(row) for row in anime_data]
        sort_time = sort_and_time(sort_function, data_sorted)
        print(f"Time taken to perform the {sort_name} on {data_size} lines is: {sort_time} seconds")
        sort_times[sort_name].append(sort_time)


fig, axs = plt.subplots(2, 2, figsize=(15, 10))


for sort_name in sort_names:
    axs[0, 0].plot(data_sizes, sort_times[sort_name], marker='o', label=sort_name)
axs[0, 0].set_xlabel('Data Size')
axs[0, 0].set_ylabel('Time (seconds)')
axs[0, 0].set_title('Time taken by sorting algorithms')
axs[0, 0].legend()


bar_width = 0.2
opacity = 0.8

for i, data_size in enumerate(data_sizes):
    for j, sort_name in enumerate(sort_names):
        axs[(i + 1) // 2, (i + 1) % 2].bar(j + bar_width, sort_times[sort_name][i], bar_width, alpha=opacity,
                                           label=sort_name)
    axs[(i + 1) // 2, (i + 1) % 2].set_xlabel('Sorting Algorithm')
    axs[(i + 1) // 2, (i + 1) % 2].set_ylabel('Time (seconds)')
    axs[(i + 1) // 2, (i + 1) % 2].set_title(f'Time taken by sorting algorithms for data size {data_size}')
    axs[(i + 1) // 2, (i + 1) % 2].set_xticks([r + bar_width for r in range(len(sort_names))])
    axs[(i + 1) // 2, (i + 1) % 2].set_xticklabels(sort_names)
    axs[(i + 1) // 2, (i + 1) % 2].legend()

plt.tight_layout()
plt.show()
