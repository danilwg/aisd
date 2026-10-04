import os
import random
import time
import json

def generate_datasets():
    os.makedirs("datasets", exist_ok=True)
    dataset_info = []
    for i in range(100):
        size = random.randint(100, 10_000)
        data = [random.randint(-100_000, 100_000) for _ in range(size)]
        filename = f"datasets/data_{i}.json"
        with open(filename, "w") as f:
            json.dump({"size": size, "data": data}, f)
        dataset_info.append((filename, size))
    return dataset_info

MIN_MERGE = 32

def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr, left, right, steps):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        steps[0] += 1
        while j >= left and arr[j] > key:
            steps[0] += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r, steps):
    len1, len2 = m - l + 1, r - m
    left = arr[l:l + len1]
    right = arr[m + 1:m + 1 + len2]

    i = j = 0
    k = l

    while i < len1 and j < len2:
        steps[0] += 1
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1

def timsort_custom(arr):
    steps = [0]
    n = len(arr)
    min_run = calc_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end, steps)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right, steps)
        size *= 2

    return steps[0]

if __name__ == "__main__":
    dataset_info = generate_datasets()
    results = []

    print(f"{'№':<4} | {'Размер (N)':<10} | {'Время (сек)':<15} | {'Итераций (Шагов)':<15}")

    for idx, (filename, size) in enumerate(dataset_info):
        with open(filename, "r") as f:
            payload = json.load(f)
            data = payload["data"]

        start_time = time.perf_counter()
        steps = timsort_custom(data)
        elapsed_time = time.perf_counter() - start_time

        results.append((size, elapsed_time, steps))
        if idx < 10:
            print(f"{idx + 1:<4} | {size:<10} | {elapsed_time:<15.6f} | {steps:<15}")