# A function that will carry out a bubble sort algorithm on a list:
def bubbleSort(list):
    for x in range(len(list)):
        for y in range(len(list) - 1):
            if list[y] > list[y + 1]:
                # Square brackets denotes the indices of the list, this is an easy way to swap elements. 'y' and 'y + 1'
                # are adjacent to one another in the list:
                list[y], list[y + 1] = list[y + 1], list[y]
    
import time
from random import randint
import numpy as np

def randomArray(n):
    array = []
    for i in range(0, n, 1):
        array.append(randint(0, n))
# Returns a randomly generated array of length n:
    return array

# Creating a function to store my results from timing bubblesort:
def times():
    start_time = time.time()
    Ar1 = randomArray(2500)
    # Calling function:
    bubbleSort(Ar1)
    end_time = time.time()
    elapsedTime = end_time - start_time
    #print(elapsedTime)

    start_time = time.time()
    Ar2 = randomArray(2500)
    bubbleSort(Ar2)
    end_time = time.time()
    elapsedTime2 = end_time - start_time
    print(elapsedTime2)

    start_time = time.time()
    Ar3 = randomArray(2500)
    bubbleSort(Ar3)
    end_time = time.time()
    elapsedTime3 = end_time - start_time
    print(elapsedTime3)

    start_time = time.time()
    Ar4 = randomArray(2500)
    bubbleSort(Ar4)
    end_time = time.time()
    elapsedTime4 = end_time - start_time
    print(elapsedTime4)

    start_time = time.time()
    Ar5 = randomArray(2500)
    bubbleSort(Ar5)
    end_time = time.time()
    elapsedTime5 = end_time - start_time
    print(elapsedTime5)

    start_time = time.time()
    Ar6 = randomArray(2500)
    bubbleSort(Ar6)
    end_time = time.time()
    elapsedTime6 = end_time - start_time
    print(elapsedTime6)

    start_time = time.time()
    Ar7 = randomArray(2500)
    bubbleSort(Ar7)
    end_time = time.time()
    elapsedTime7 = end_time - start_time
    print(elapsedTime7)

    start_time = time.time()
    Ar8 = randomArray(2500)
    bubbleSort(Ar8)
    end_time = time.time()
    elapsedTime8 = end_time - start_time
    print(elapsedTime8)

    start_time = time.time()
    Ar9 = randomArray(2500)
    bubbleSort(Ar9)
    end_time = time.time()
    elapsedTime9 = end_time - start_time
    print(elapsedTime9)

    start_time = time.time()
    Ar10 = randomArray(2500)
    bubbleSort(Ar10)
    end_time = time.time()
    elapsedTime10 = end_time - start_time
    print(elapsedTime10)

    final_result = ((elapsedTime+elapsedTime2+elapsedTime3+elapsedTime4+elapsedTime5+elapsedTime6+elapsedTime7+elapsedTime8+elapsedTime9+elapsedTime10) / 10) * 1000
    print("Average time in milliseconds: {:.3f}".format(final_result))

# Whatever is specified under 'name == main' will make the program carry that out first:
if __name__ == "__main__":
    times()
    import timeit
    Ar2 = randomArray(100)
    num_runs = 10
    # I had to make bubbleSort(Ar1) a string using 'str', to solve an error (ValueError: stmt is neither a string nor callable).
    duration = timeit.Timer(str(bubbleSort(Ar2))).timeit(number = num_runs)
    avg_duration = duration / num_runs
    print(duration)
    # Using 'f-string literal' method here in the print statement, passing in 'avg_duration' as an argument:
    print(f'On average it took {avg_duration} seconds')
    print("Over the 10 runs the average time was {}".format(avg_duration))
