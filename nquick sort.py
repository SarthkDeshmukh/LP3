import random, time

def quick_sort(arr, randomized=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)] if randomized else arr[-1]
    left, right = [x for x in arr if x < pivot], [x for x in arr if x > pivot]
    return quick_sort(left, randomized) + [pivot] + quick_sort(right, randomized)

def analyze_sorting():
    n = int(input("Enter number of elements: "))
    arr = [random.randint(1, 1000) for _ in range(n)]
    print("Original array:", arr)

    for method in ["Deterministic", "Randomized"]:
        start = time.time()
        sorted_arr = quick_sort(arr.copy(), randomized=(method == "Randomized"))
        print(f"\n{method} QuickSort result:", sorted_arr)
        print(f"Time taken by {method} QuickSort: {time.time() - start:.6f} seconds")

analyze_sorting()
