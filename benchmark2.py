from cProfile import label
import bubblesort
import bucketsort
import introsort2
import quicksort2
import timsort
from random import sample
from random import randint
import time


def randomArray(n):
# Initializing an empty array:
    array = []
# Creating a for loop and specifying a range of 0 to n with a stepsize of 1. 'randint' method generates random numbers
# Randint was imported on line 8:
    for i in range(0, n, 1):
        array.append(randint(0, n))
# Returns a randomly generated array of length n:
    return array

# Using a for loop inside a form loop in a function for trialling an algorithm 10 times for different input instances:
def times_a():
    numRuns = 10
    results = []
    for x in range(numRuns):
        sum = 0
        n = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000]
        for a in n:
            start_time = time.time()
            array3 = randomArray(a)
            bucketsort.bucket1(array3)
            end_time = time.time()
            elapsed = end_time - start_time  
            results.append(elapsed)
            for result in results:
                total = (sum + results[result]) / 10
        print("{:.12f}".format(total))


numRuns = 10
results = []
for x in range(numRuns):
    sum = 0
# 'time.time()' is called here to start a timer before calling an algorithm on a specified array. The previously
# defined function 'randomArray' is used to create an array of randomly distributed numbers up to the number passed
# into it:
    start_time = time.time()
    array3 = randomArray(120)
# The array is passed into the algorithm (bubbleSort) defined on the imported page 'bubblesort':
    bubblesort.bubbleSort(array3)
# 'time.time()' is called again after running the algorithm on the array, allowing the user to calculate the time it
# took to sort the array:
    end_time = time.time()
    elapsed = end_time - start_time  
# The times are then added in to the empty results array defined above using the .append() method:
    results.append(elapsed)
    for result in range(0, len(results)):
# Creating a varibale name will make it easier when using this result later. The 10 runs are added together and to the
# sum variable which was set to zero. This is divided by 10 to get the average time in seconds, or multiplying the calculation
# by a 1000 outputs the result in milliseconds:
        tot1a = ((sum + results[result]) / 10) * 1000
# The code is mostly the same in these next for loops, except different array sizes (n) are trialled, as well as calling
# the other algorithms on the arrays. The variable name for each result must also be different to avoid confusion, and 
# to make sure the user can use all the results in other code:
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(300)
    bubblesort.bubbleSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot1b = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(700)
    bubblesort.bubbleSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot1c = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(1500)
    bubblesort.bubbleSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot1d = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(3500)
    bubblesort.bubbleSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot1e = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(8000)
    bubblesort.bubbleSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot1f = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(16500)
    bubblesort.bubbleSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot1g = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    sum = 0
    start_time = time.time()
    array3 = randomArray(120)
    bucketsort.bucket1(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot2a = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(300)
    bucketsort.bucket1(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot2b = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(700)
    bucketsort.bucket1(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot2c = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(1500)
    bucketsort.bucket1(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot2d = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(3500)
    bucketsort.bucket1(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot2e = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(8000)
    bucketsort.bucket1(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot2f = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(16500)
    bucketsort.bucket1(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot2g = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    sum = 0
    start_time = time.time()
    array3 = randomArray(120)
    introsort2.intro_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot3a = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(300)
    introsort2.intro_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot3b = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(700)
    introsort2.intro_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot3c = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(1500)
    introsort2.intro_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot3d = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(3500)
    introsort2.intro_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot3e = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(8000)
    introsort2.intro_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot3f = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(16500)
    introsort2.intro_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot3g = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    sum = 0
    start_time = time.time()
    array3 = randomArray(120)
    quicksort2.QuickSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot4a = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(300)
    quicksort2.QuickSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot4b = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(700)
    quicksort2.QuickSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot4c = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(1500)
    quicksort2.QuickSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot4d = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(3500)
    quicksort2.QuickSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot4e = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(8000)
    quicksort2.QuickSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot4f = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(16500)
    quicksort2.QuickSort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot4g = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    sum = 0
    start_time = time.time()
    array3 = randomArray(120)
    timsort.tim_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot5a = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(300)
    timsort.tim_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot5b = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(700)
    timsort.tim_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot5c = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(1500)
    timsort.tim_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot5d = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(3500)
    timsort.tim_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot5e = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(8000)
    timsort.tim_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot5f = ((sum + results[result]) / 10) * 1000
for x in range(numRuns):
    start_time = time.time()
    array3 = randomArray(16500)
    timsort.tim_sort(array3)
    end_time = time.time()
    elapsed = end_time - start_time  
    results.append(elapsed)
    for result in range(0, len(results)):
        tot5g = ((sum + results[result]) / 10) * 1000


# Storing a .txt file in a variable:
filename = "results5.txt"
# Passing in the defined variable and 'w' meaning write into the .open() method. This creates a file and allows the 
# user to write data to it:
file = open(filename, 'w')
file.write("Times Recorded in Milliseconds")
file.write("\n--------------------------------------------------------------------------------------------")
file.write("\n   Size     |   120     |    3000    |    700    |   1500   |   3500   |  8000   |   16500  ")
# Using .format() method to modify the presentation of the times recorded for the algorithms. Replacement fields are
# denoted with curly brackets inside quotes. Using automatic formatting here, in which there must be at least at many 
# arguments passed into .format() as there are replacement fields.'f' for 'floating point' is used to specify the number 
# of digits after the decimal point. ':' is used as a separator in replacement fields:
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nBubble Sort |  {:.3f}  |  {:.3f}  | {:.3f}  |  {:.2f}   |    {:.2f}  ".format(tot1a, tot1b, tot1c, tot1d, tot1e))
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nBucket Sort | {:.7f}|{:.7f}| {:.5f} | {:3f}| {:3f}| {:3f}| {:3f}".format(tot2a, tot2b, tot2c, tot2d, tot2e, tot2f, tot2g))
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nIntro Sort  | {:.7f}|{:.7f} | {:.3f}  |  {:.3f}  | {:.3f}  | {:.3f}  |  {:.3f} ".format(tot3a, tot3b, tot3c, tot3d, tot3e, tot3f, tot3g))
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nQuick Sort  |  {:.6f} |  {:.6f}  | {:.4f} | {:.3f} |  {:.3f} | {:.3f}  | {:.3f} ".format(tot4a, tot4b, tot4c, tot4d, tot4e, tot4f, tot4g))
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nTim Sort    |{:.7f}| {:.7f}|  {:.5f}   | {:.3f}  |  {:.3f}  |   {:.3f}  |  {:.3f}  ".format(tot5a, tot5b, tot5c, tot5d, tot5e, tot5f, tot5g))


#n = [120, 300, 700, 1500, 3500, 8000, 16500]
n = [120, 300, 700, 1500, 3500]
arrBub = [tot1a, tot1b, tot1c, tot1d, tot1e]
arrBuck = [tot2a, tot2b, tot2c, tot2d, tot2e]
arrInt = [tot3a, tot3b, tot3c, tot3d, tot3e]
arrQui = [tot4a, tot4b, tot4c, tot4d, tot4e]
arrTim = [tot5a, tot5b, tot5c, tot5d, tot5e]


import matplotlib.pyplot as plt
import numpy as np
plt.plot(n, arrBub, color='r', label='Bubble Sort')
plt.plot(n, arrBuck, color='b', label='Bucket Sort')
plt.plot(n, arrInt, color='y', label='Intro Sort')
plt.plot(n, arrQui, color='g', label='Quick Sort')
plt.plot(n, arrTim, label='Tim Sort')
plt.legend()
# The np.arange method returns evenly spaced values within an interval using a stepsize:
plt.xticks(np.arange(0,3200,200))
# Range was of 0 - 3 was too low here, y axis values squashed & still unable to compare the lines bar bubble.
plt.yticks(np.arange(0,12,0.8))
plt.ylabel("Running times (milliseconds)")
plt.xlabel("Input Sizes")
plt.title("Line Plot without Bubble Sort")
# The .savefig() method must be before the .show() method, otherwise .show() will prevent the next line of code
# doing anything with the image:
plt.savefig("line_plt2")
plt.show()


# https://eldoyle.github.io/PythonIntro/08-ReadingandWritingTextFiles/
filename = "results2.txt"
file = open(filename, 'w')
file.write("   Size     |   100     |   250    |  500   |  750    |  1000   |   1250   |   2500  |  3750   |  5000  ")
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nBubble Sort | {}    |  {}  | {}| {} | {}  | {} | {}| {}| {}".format(arrBub[0], arrBub[1], arrBub[2], arrBub[3], arrBub[4], arrBub[5], arrBub[6], arrBub[7], arrBub[8]))
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nBucket Sort | {:.8f}| {:.8f}| {:.4f} | {:4f}| {:4f}| {:4f}| {:4f}| {:4f}| {:4f}".format(float(arrBuck[0]), float(arrBuck[1]), float(arrBuck[2]), float(arrBuck[3]), float(arrBuck[4]), float(arrBuck[5]), float(arrBuck[6]), float(arrBuck[7]), float(arrBuck[8])))
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nIntro Sort  | {:.6f}  |  {:.4f}   | {:.3f}  |  {:.3f}  | {:.3f}  | {:.3f}  |  {:.3f} |  {:.3f}  | {:.3f}".format(float(arrInt[0]), float(arrInt[1]), float(arrInt[2]), float(arrInt[3]), float(arrInt[4]), float(arrInt[5]), float(arrInt[6]), float(arrInt[7]), float(arrInt[8])))
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nQuick Sort  |  {}  |  {}  | {}| {}| {}| {} | {} | {} | {}".format(arrQui[0], arrQui[1], arrQui[2], arrQui[3], arrQui[4], arrQui[5], arrQui[6], arrQui[7], arrQui[8]))
file.write("\n------------|----------------------------------------------------------------------------------------")
file.write("\nTim Sort    | {:.8f}|   {:.4f}  | {:.3f}  | {:.3f}  | {:.3f}  |  {:.3f}  |  {:.3f}  |  {:.3f} | {:.3f}".format(float(arrTim[0]), float(arrTim[1]), float(arrTim[2]), float(arrTim[3]), float(arrTim[4]), float(arrTim[5]), float(arrTim[6]), float(arrTim[7]), float(arrTim[8])))


if __name__ == "__main__":
    times_a()