import random

# QuickSort Algorithm Implementation (In-place, space-optimal)
#
# Input:
#   - array: a list of integers (duplicates allowed)
# Output:
#   - the input list is sorted in-place in ascending order
#
# Features:
#   - Average runtime: O(n log n)
#   - In-place: sorts the list without allocating new lists
#   - Uses random pivot selection to avoid worst-case performance on sorted input
#   - Partitioning is done by rearranging elements around the pivot
#
# Points of Concern:
#   - The algorithm is not stable (relative order of equal elements is not preserved)
#   - Handles duplicate values correctly
#   - Space-optimal: only uses O(log n) stack space due to recursion

def QSort(array, left=0, right=None):
    """
    In-place QuickSort algorithm. Sorts the array between indices left and right.

    Parameters:
        array (list): List of integers to sort.
        left (int): Left index (inclusive).
        right (int): Right index (exclusive).

    Returns:
        list: The same list, sorted in-place.
    """
    if right is None:
        right = len(array)
    if right - left <= 1:
        return array
    pivot_idx = random_pivot(array, left, right)
    pivot_new_idx = partition(array, left, right, pivot_idx)
    QSort(array, left, pivot_new_idx)
    QSort(array, pivot_new_idx + 1, right)
    return array

def partition(array, left, right, pivot_idx):
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
    array[left], array[pivot_idx] = array[pivot_idx], array[left]
    pivot = array[left]
    i = left + 1
    for j in range(left + 1, right):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[left], array[i - 1] = array[i - 1], array[left]
    return i - 1

def random_pivot(array, left, right):
    return random.randint(left, right - 1)

def test_case():
    P = [8, 6, 4, 2, 7, 5, 3, 1, 4, 6, 2, 8]
    QSort(P)
    print(P == sorted(P))
    print(P)
test_case()
