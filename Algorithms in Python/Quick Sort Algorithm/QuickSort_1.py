# Content: 
# The first implementation of the QuickSort algorithm

# Input: an unsorted array of distinct integers 
#   Note: Can accomendate duplicates 
#   Representation: a list of integers
# Output: sorted version of the array
# Interesting Features:
#   (i) Has runtime = O(nlogn)
#   (ii) Works in place i.e. No extra memory required 


def QSort(array):
    n = len(array)

    if n <= 1:
        return array
    else:
        pivot_idx = random_pivot(array)
        res = partition(array, pivot_idx)
        fir_sorted, pivot, sec_sorted = QSort(res[0]), res[1], QSort(res[2])
        return fir_sorted + [pivot] + sec_sorted

def partition(array, pivot_idx):
    n = len(array)
    array[0], array[pivot_idx] = array[pivot_idx], array[0]

    i = 1 
    for j in range(1, n):
        if array[j] < array[0]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[0], array[i-1] = array[i-1], array[0]
    return (array[:i-1], array[i-1], array[i:])

import random 
def random_pivot(array):
    n = len(array)
    return random.randint(0, n-1)

def test_case():
    P = [8, 6, 4, 2, 7, 5, 3, 1, 2, 3]
    print([1, 2, 2, 3, 3, 4, 5, 6, 7, 8] == QSort(P))
    print(QSort(P))
test_case()