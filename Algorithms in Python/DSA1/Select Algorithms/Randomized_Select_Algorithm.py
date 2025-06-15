# Goal: Implement the Randomized Select Algorithm
# Input: an unsorted array A of n distinct integers, and an integer m
# Output: the mth order statistic of A

# Aims:
#   (i) Achieve average O(n) runtime 
#   (ii) Works in place, achieve optimal space usage

def RSelect(array, m, left=0, right=None):
    if right is None:
        right = len(array)
    n = right - left

    if n <= 1:
        return array[left]
    else:
        random_idx = random_pivot(left, right)
        pivot_idx = partition(array, random_idx, left, right)  # <-- updated argument order
        k = pivot_idx - left 

        if m == k:
            return array[pivot_idx]
        elif m < k:
            return RSelect(array, m, left, pivot_idx)
        else:
            return RSelect(array, m - k - 1, pivot_idx + 1, right)

def partition(array, pivot_idx, left = 0, right = None):
    """
    Lomuto partition scheme for in-place partitioning.

    Parameters:
        array (list): List of integers to partition.
        left (int): Left index (inclusive).
        right (int): Right index (exclusive).
        pivot_idx (int): Index of the pivot element.

    Returns:
        int: The final index of the pivot.
    """
    if right is None:
        right = len(array)

    array[left], array[pivot_idx] = array[pivot_idx], array[left]
    pivot = array[left]
    i = left + 1
    for j in range(left + 1, right):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[left], array[i - 1] = array[i - 1], array[left]
    return i - 1

import random
def random_pivot(left, right):
    return random.randint(left, right - 1)

# Test Case #
def test_case():
    P = [8, 7, 6, 4, 3, 5, 1, 2, 12, 15, 9, 10, 13, 11, 14, 16, 17, 18, 19, 20]
    order_stat = 11  
    res = RSelect(P, order_stat)
    expected = sorted(P)[order_stat]
    print(f"The expected answer {expected} matches RSelect result? {expected == res}!")
    if not expected == res:
        print(f"The incorrect output from DSelect is {res}")

if __name__ == "__main__":
    # Only runs when this file is executed directly
    print("Testing RSelect...")
    # test cases here
    test_case()