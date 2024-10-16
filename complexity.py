import time
import random


# O(1) - constant complexity
print(f'\n=== O(1) - constant complexity ===\n')

def getElement(arr, index):
    return arr[index]

#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_size = 1000
arr = [random.randint(1, 10000) for _ in range(array_size)]

start_time = time.time()
result = getElement(arr, 4)
end_time = time.time()
execution_time = end_time - start_time

print("Element:", result)
print("Execution time:", execution_time, "sec")

# O(n) - linear complexity
print(f'\n=== O(n) - linear complexity ===\n')

def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#arr = [10, 20, 30, 40, 50]

array_size = 1000
arr = [random.randint(1, 10000) for _ in range(array_size)]

target_number = random.randint(1, 10000)
start_time = time.time()
result = line_search(arr, target_number)
end_time = time.time()
execution_time = end_time - start_time

print(f"Result for line_search: {result}")
print(f"Execution time for {array_size} element: {execution_time} sec")

# O(log n) - logarithmic complexity
print(f'\n=== O(log n) - logarithmic complexity ===\n')

def binary_search(arr, target):
    low, high = 0, len(arr)- 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array_size = 1_000
arr = [random.randint(1, 10000) for _ in range(array_size)]
arr.sort()
# print(arr)

target_number = random.randint(1, 10000)
start_time = time.time()
result = binary_search(arr, target_number)
end_time = time.time()
execution_time = end_time - start_time

print(f"Result for binary_search: {result}")
print(f"Execution time for {array_size} element: {execution_time} sec")
