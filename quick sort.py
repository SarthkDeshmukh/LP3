import random
import time

def quick_sort(arr, low, high, randomized=False):
    if low < high:
        pivot_index = randomized_partition(arr, low, high) if randomized else partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1, randomized)
        quick_sort(arr, pivot_index + 1, high, randomized)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[low], arr[random_index] = arr[random_index], arr[low]
    return partition(arr, low, high)

def time_sorting(sort_function, arr):
    start_time = time.time()
    sort_function(arr, 0, len(arr) - 1)
    return time.time() - start_time

def main():
    n = 100000
    arr = [random.randint(1, 1000000) for _ in range(n)]
    
    arr_deterministic = arr.copy()
    time_deterministic = time_sorting(quick_sort, arr_deterministic)
    print(f"Deterministic Quick Sort Time: {time_deterministic:.6f} seconds")
    
    time_randomized = time_sorting(quick_sort, arr)
    print(f"Randomized Quick Sort Time: {time_randomized:.6f} seconds")

if __name__ == "__main__":
    main()
