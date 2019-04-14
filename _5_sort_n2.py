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
            arr[j + 1] = arr[0]
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
