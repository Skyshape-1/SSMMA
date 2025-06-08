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

