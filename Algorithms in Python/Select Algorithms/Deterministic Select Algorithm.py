import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Merge_Sort import merge_sort
from Randomized_Select_Algorithm import partition
# Purpose: Implement the DSelect algorithm taught in Module 3
# Input: an unsorted array A of n distinct integers, and an integer m (0-based)
# Output: the mth order statistic of A
# Remarks:
#   (i) Achieves linear runtime
#   (ii) Works with extra memory (not in place) due to recursive calls

def DSelect(array, m):
    n = len(array)
    if n == 1:
        return array[0]
    copy = array.copy()  # Shallow copy but sufficient

    # 1. Break A into groups of 5 and collect medians in sub_grp_medians
    sub_grp_medians = []
    arr = copy.copy()  # Work on a copy so we don't mutate the input
    while len(arr) >= 5:
        tem = merge_sort(arr[:5])
        del arr[:5]
        sub_grp_medians.append(tem[2])
    if len(arr) > 0:
        last = merge_sort(arr)
        last_med = last[len(arr)//2]
        sub_grp_medians.append(last_med)

    # 2. Recursively find the median of sub_grp_medians
    median_of_meds = DSelect(sub_grp_medians, len(sub_grp_medians)//2)

    # 3. Partition around the pivot found in 2
    pivot_idx = copy.index(median_of_meds)
    pivot_idx_sorted = partition(copy, pivot_idx)

    # 4. Recursively call to simplify the problem
    if pivot_idx_sorted == m:
        return copy[pivot_idx_sorted]
    elif pivot_idx_sorted > m:
        return DSelect(copy[:pivot_idx_sorted], m)
    else:
        return DSelect(copy[pivot_idx_sorted + 1:], m - pivot_idx_sorted - 1)

def test_case():
    P = [8, 7, 6, 4, 3, 5, 1, 2, 12, 15, 9, 10, 13, 11, 14, 16, 17, 18, 19, 20]
    order_stat = 11  # 0-based: 11th smallest is 12
    res = DSelect(P, order_stat)
    expected = sorted(P)[order_stat]
    print(f"The expected answer {expected} matches DSelect result? {expected == res}!")
    if not expected == res:
        print(f"The incorrect output from DSelect is {res}")

if __name__ == "__main__":
    # Only runs when this file is executed directly
    print("Testing DSelect...")
    # test cases here
    test_case()