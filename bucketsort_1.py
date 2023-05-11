# https://www.programiz.com/dsa/bucket-sort
def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


import time
import random
from random import randint
 
# Python code to perform a bucket sort on an array. This code worked better and I used in in benchmark.py:
# https://coderslegacy.com/python/bucket-sort-algorithm/
def bucket1(array):
    largest = max(array)
    length = len(array)
    size = largest/length
 
    # Create Buckets
    buckets = [[] for i in range(length)]
 
    # Bucket Sorting   
    for i in range(length):
        index = int(array[i]/size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])
 
    # Sorting Individual Buckets  
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])
 
 
    # Flattening the Array
    result = []
    for i in range(length):
        result = result + buckets[i]
    return result
 
arr = [5, 44, 20, 7, 68, 55, 33, 1, 17, 50, 15, 32]
output = bucket1(arr)
#print(output)