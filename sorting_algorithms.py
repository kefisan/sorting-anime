import random

global column
column = None


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and int(data[j][column]) > int(key[column]):
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
        while data[i][column] < pivot[column]:
            i += 1
        j -= 1
        while data[j][column] > pivot[column]:
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
    if left < n and int(data[i][column]) < int(data[left][column]):
        largest = left
    if right < n and int(data[largest][column]) < int(data[right][column]):
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
        index = (int(data[i][column]) // exp1)
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (int(data[i][column]) // exp1)
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
    data[:] = output[:]


def radix_sort(data):
    max1 = max(int(row[column]) * 100 for row in data)
    exp = 1
    while max1 // exp > 0:
        counting_sort(data, exp)
        exp *= 10
