import time
import math

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

def count_run_and_make_ascending(arr, left, right, steps):
    if left >= right:
        return 1

    run_end = left + 1
    if run_end > right:
        return 1

    if arr[run_end] < arr[run_end - 1]:
        steps[0] += 1
        while run_end <= right and arr[run_end] < arr[run_end - 1]:
            steps[0] += 1
            run_end += 1
        arr[left:run_end] = arr[left:run_end][::-1]
    else:
        steps[0] += 1
        while run_end <= right and arr[run_end] >= arr[run_end - 1]:
            steps[0] += 1
            run_end += 1

    return run_end - left


def merge(arr, l, m, r, steps):
    len1, len2 = m - l + 1, r - m
    left_arr = arr[l:l + len1]
    right_arr = arr[m + 1:m + 1 + len2]

    i = j = 0
    k = l

    while i < len1 and j < len2:
        steps[0] += 1
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def timsort_custom(arr):
    steps = [0]
    n = len(arr)
    if n < 2:
        return steps[0]

    min_run = calc_min_run(n)
    runs = []

    i = 0
    while i < n:
        run_len = count_run_and_make_ascending(arr, i, n - 1, steps)

        if run_len < min_run:
            target_len = min(min_run, n - i)
            insertion_sort(arr, i, i + target_len - 1, steps)
            run_len = target_len

        runs.append((i, run_len))
        i += run_len

    while len(runs) > 1:
        new_runs = []
        idx = 0
        while idx < len(runs) - 1:
            l1, len1 = runs[idx]
            l2, len2 = runs[idx + 1]
            merge(arr, l1, l1 + len1 - 1, l1 + len1 + len2 - 1, steps)
            new_runs.append((l1, len1 + len2))
            idx += 2
        if idx < len(runs):
            new_runs.append(runs[idx])
        runs = new_runs

    return steps[0]