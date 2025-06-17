### Question Statement ###
# Given an array of n distinct (but unsorted) elements x1, x2, ..., xn with positive weights: 
#                                                      w1, w2, ..., wn such that ∑{i=1,n}(wi) = W. 
# 
# A "weighted median" is an element xk for which the total weight of all elements 
#     (1) the total weight of elements with value SMALLER than xk (i.e., ∑{xi < xk} wi) is at most W/2, 
#     (2) the total weight of elements with value LARGER than xk (i.e., ∑{xi > xk} wi) is at most W/2.
#  
# Observe that there are at most two weighted medians. 
# Show how to compute all weighted medians in O(n) worst-case time.


##### Analysis #####:
# If we can sort the list by weights wi,  --- O(n log n)
# and then accumlate total_weight iteratively --- O(n)
# Then we can achieve our goal in O(n log n) time
# Conclusion:
# However, as we are aiming for linear runtime, we have to use PARTITION.


##### Second try: Median Pivot Choice #####
# Preprocessing:
#   Find W --- O(n)
# (1) Choose the median of X as pivot using DSelect--- O(n)
#       Initiate left & right to record accumulative totals for weights
# (2) Partition P according to x-values around the pivot --- O(n)
# (3) Add up the weights on smaller values of xj (left of pivot), denoted by Wl
#    check if Wl and (1-Wl-weight of pivot) are smaller than W/2, if both yes, then return pivot
#    else continue                    --- O(n/2)
# (4) Choose the side with larger than W/2 total weight and repeat this above process
#   P.S. Each round when comparing total weights, need to account for parts of the list left 
#        behind previously

### So the million dollar question is...
# What's the expected runtime of this algorithm???

# According to our master method
# a = 1, b = 2, d = 1 [O(n)]
# a < b^d, thus the running time of this algorithm is O(n^d) == O(n)


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Select_Algorithms.Deterministic_Select_Algorithm import DSelect
# from Select_Algorithms.Randomized_Select_Algorithm import partition


def find_weighted_median(xwarray, left=0, right=0, W=None):
    xarray = list(map(lambda pair: pair[0], xwarray))
    warray = list(map(lambda pair: pair[1], xwarray))
    if W is None:
        W = sum(warray)  # Total weights
    pivot_median = find_median(xarray)  # Return x-value of the median WithOut its idx
    pivot_raw_idx = xarray.index(pivot_median)  # x-values are guaranteed to be distinct
    pivot_weight = warray[pivot_raw_idx]
    pivot_sor_idx = weighted_partition(xwarray, pivot_raw_idx)

    p_xarray = list(map(lambda pair: pair[0], xwarray))
    p_warray = list(map(lambda pair: pair[1], xwarray))

    # Summing partial weights
    tem_left = left + sum(p_warray[:pivot_sor_idx])
    tem_right = right + sum(p_warray[pivot_sor_idx + 1:])
    if tem_left > W / 2:
        # Recurse on left part, exclude pivot
        return find_weighted_median(xwarray[:pivot_sor_idx], left, tem_right + pivot_weight, W)
    elif tem_right > W / 2:
        # Recurse on right part, exclude pivot
        return find_weighted_median(xwarray[pivot_sor_idx + 1:], tem_left + pivot_weight, right, W)
    else:
        return pivot_median  # For the sake of simplicity, we are ignoring cases of bi-medians


# Needs prior testins to ensure its functionality
#   (1) returns pivot's index in partitioned array
#   (2) partitions the array by the pivot's x-value
def weighted_partition(xwarray, pivot_idx, left = 0, right = None):
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
        right = len(xwarray)

    xwarray[left], xwarray[pivot_idx] = xwarray[pivot_idx], xwarray[left]
    pivot = xwarray[left][0]
    i = left + 1
    for j in range(left + 1, right):
        if xwarray[j][0] < pivot:
            xwarray[i], xwarray[j] = xwarray[j], xwarray[i]
            i += 1
    xwarray[left], xwarray[i - 1] = xwarray[i - 1], xwarray[left]
    return i - 1

def find_median(xarray): # Wrapper function around DSelect
    n = len(xarray)
    return DSelect(xarray, n//2)


def test():
    test_cases = [
        {
            "name": "Simple test case",
            "array": [(2, 0.2), (4, 0.4), (1, 0.1), (5, 0.5), (3, 0.3)]
        },
        {
            "name": "Complex test case",
            "array": [
                (30, 0.15), (40, 0.2), (50, 0.25), (10, 0.05), (20, 0.1),
                (80, 0.4), (90, 0.45), (60, 0.3), (70, 0.35), (100, 0.5)
            ]
        }
    ]

    for case in test_cases:
        print(f"===== {case['name']} =====")
        print("Input weighted array:", case['array'])
        median = find_weighted_median(case['array'].copy())
        print("Weighted median:", median)
        print()


if __name__ == "__main__":
    test()

    ######
    # I suspect the root cause of infinite recursion lies in me trying to include the pivot(former median)
    # when I call recursive calls, length of sub-xwarrays are stuck somewhere
    
    # Mind that this suspicion is to be confirmed, I gotta rest now.