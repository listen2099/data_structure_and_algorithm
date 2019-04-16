import random

# 1 2 3 4 5
# bobble
arr = [random.randrange(10, 100) for _ in range(10)]
print('origin', arr)


def bobble(arr):
    length = len(arr)
    for i in range(length):
        is_switch = False
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_switch = True
        if not is_switch:
            break
    print('bobble', arr)


arr = [random.randrange(10, 100) for _ in range(10)]

bobble(arr)

# insertion
arr = [random.randrange(10, 100) for _ in range(10)]
print('origin', arr)
arr = [0] + arr


def insertion(arr):
    length = len(arr)
    for i in range(1, length):
        arr[0] = arr[i]
        j = i - 1
        if arr[j] > arr[0]:
            while arr[0] < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = arr[0]  # 关键要注意j的位置, 插入的位置应该是j+1
    print('insertion', arr[1:])


insertion(arr)

# selection
arr = [random.randrange(10, 100) for _ in range(10)]
print('origin', arr)


def selection(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    print('selection', arr)


selection(arr)
# 0 1 2 3 4
# j

# 实现归并排序
from typing import List

arr = [random.randrange(10, 100) for _ in range(10)]
print('origin', arr)


def merge_sort(arr: List[int]):
    merge_sort_c(arr, 0, len(arr) - 1)


def merge_sort_c(arr: List[int], low: int, high: int):
    if low < high:
        mid = (low + high) // 2
        merge_sort_c(arr, low, mid)
        merge_sort_c(arr, mid + 1, high)
        merge(arr, low, mid, high)


def merge(arr: List[int], low: int, mid: int, high: int):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(arr[start:end + 1])
    arr[low:high + 1] = tmp


merge_sort(arr)
print('merge', arr)

# 实现快速排序


# 在O(n)时间复杂度找出无序数组中第K大元素
