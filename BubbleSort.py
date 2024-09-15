# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:47:54 2024

@shery: hp
"""

import random
import time
import csv

def randomArray(size):
    """Generate an array of random integers between 0 and 10000."""
    Arr = []
    for _ in range(size):
        Arr.append(random.randint(0, 10000))
    return Arr

def bubblesort(arr, start, end):
    """Sort the array using the bubble sort algorithm."""
    for i in range(end - start):
        swapped = False
        # Traverse the array from start to end - i - 1
        for j in range(start, end - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break

size = 30000
result = randomArray(size)
print(f"Random array of size {size}: {result}")

start_time = time.time()
bubblesort(result, 0, size)
end_time = time.time()

print("Sorted array:", result)
print("Runtime is", end_time - start_time, "seconds")

with open("SortedArray.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sorted Array"])
    for i in result:
        writer.writerow([i])
