                                        ### Question Statement ###
# Given an array of n distinct (but unsorted) elements x1, x2, ..., xn with positive weights: 
#                                                      w1, w2, ..., wn such that ∑{i=1,n}(wi) = W. 
# 
# A "weighted median" is an element xk for which the total weight of all elements 
#     (1) the total weight of elements with value SMALLER than xk (i.e., ∑{xi < xk} wi) is at most W/2, 
#     (2) the total weight of elements with value LARGER than xk (i.e., ∑_{xi > xk} wi) is at most W/2.
#  
# Observe that there are at most two weighted medians. 
# Show how to compute all weighted medians in O(n) worst-case time.

# Input Representation: A list of n tuples, each containing (xi, wi)
P = [(1,0.1), (2, 0.2), (3, 0.3), (4, 0.4), (5, 0.5)]
# In this example, W = 0.1 + 0.5 + 0.9 + 1.6 + 2.5 = 5.6
# The weighted median(s) is(are) x4 = 4

# Analysis:
# If we can sort the list by weights wi,  --- O(n log n)
# and then accumlate total_weight iteratively --- O(n)
# Then we can achieve our goal in O(n log n) time

# However, as we are aiming for linear runtime, we have to use PARTITION.

# First try: Random Pivot Choice
# Preprocessing:
#   Find W --- O(n)
# (1) Randomly choose a pivot among X --- O(1)
# (2) Partition P according to x-values around the pivot --- O(n, length of array to be partitioned)
# (3) Add up the weights on smaller values of xj (left of pivot), denoted by Wl
#    check if Wl and (1-Wl-weight of pivot) are smaller than W/2, if both yes, then return pivot
#    else continue                    --- O(?)
# (4) Choose the side with larger than W/2 total weight and repeat this above process
#   P.S. Each round when comparing total weights, need to account for parts of the list left behind previously

### So the million dollar question is...
# What's the expected runtime of this algorithm???