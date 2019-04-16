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
        if arr[i] <= arr[j]:  # 归并排序的精髓就是在合并的时候顺便排序
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

from typing import List
import random


def quick_sort(a: List[int]):
    _quick_sort_between(a, 0, len(a) - 1)


def _quick_sort_between(a: List[int], low: int, high: int):
    if low < high:
        # get a random position as the pivot
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]

        m = _partition(a, low, high)  # a[m] is in final position
        _quick_sort_between(a, low, m - 1)
        _quick_sort_between(a, m + 1, high)


def _partition(a: List[int], low: int, high: int):
    pivot, j = a[low], low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]  # swap
    a[low], a[j] = a[j], a[low]
    return j


def test_quick_sort():
    a1 = [3, 5, 6, 7, 8]
    quick_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)


# 在O(n)时间复杂度找出无序数组中第K大元素

def partition(data_list, begin, end):
    # 选择最后一个元素作为分区键
    partition_key = data_list[end - 1]

    # index为分区键的最终位置
    index = begin
    for i in range(begin, end - 1):
        if data_list[i] < partition_key:
            data_list[i], data_list[index] = data_list[index], data_list[i]  # 交换
            index += 1

    data_list[index], data_list[end - 1] = data_list[end - 1], data_list[index]  # 交换
    return index


def find_top_k(data_list, K):
    length = len(data_list)
    begin = 0
    end = length
    index = partition(data_list, begin, end)  # 这里的partition函数就是上面快排用到的函数
    while index != length - K:
        if index > length - K:
            index = partition(data_list, begin, index)
        else:
            index = partition(data_list, index + 1, end)
    return data_list[index]


data_list = [25, 77, 52, 49, 85, 28, 1, 28, 100, 36]
print(data_list)
for i in [1, 2, 3, 4, 5]:
    print(f"第 {i} 大元素是 {find_top_k(data_list, i)}")
