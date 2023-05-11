# Python code using a recursive method to benchmark the quick sort algorithm:
# https://www.educative.io/edpresso/how-to-implement-quicksort-in-python

def QuickSort(arr):

    elements = len(arr)
    # Base case:
    if elements < 2:
        return arr
    # Position of the partitioning element:
    current_position = 0 
    # Partitioning loop:
    for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    # Brings pivot to it's appropriate position: 
    arr[current_position] = temp 
    # Sorts the elements to the left of pivot:
    left = QuickSort(arr[0:current_position]) 
    # Sorts the elements to the right of pivot:
    right = QuickSort(arr[current_position+1:elements]) 
    # Merging everything together:
    arr = left + [arr[current_position]] + right
    
    return arr
