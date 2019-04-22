# Counting sort

import random

arr = [random.randrange(10, 100) for _ in range(10000)]
print('origin', arr[1:20])


def countingsort(arr):
    length = len(arr)
    if length <= 1:
        return -1

    max = arr[0]
    for i in range(length):
        if arr[i] > max:
            max = arr[i]

    c = [0] * (max + 1)

    for i in range(length):
        c[arr[i]] += 1

    for i in range(1, max + 1):
        c[i] = c[i - 1] + c[i]

    r = [0] * length
    for i in range(length - 1, -1, -1):
        index = c[arr[i]] - 1
        r[index] = arr[i]
        c[arr[i]] -= 1
    for i in range(length):
        arr[i] = r[i]
    return r


print(countingsort(arr)[9960:10000])
