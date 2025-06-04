                                    ### Question Statement ###
# You are given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than 
# all of its neighbors. (A neighbor of a number is one immediately above, below, to the left, or 
# the right. Most numbers have four neighbors; numbers on the side have three; the four corners have two.) 
# Use the divide-and-conquer algorithm design paradigm to compute a local minimum with only O(n) 
# comparisons between pairs of numbers. (Note: since there are n² numbers in the input, you cannot 
# afford to look at all of them. Hint: Think about what types of recurrences would give you
# the desired upper bound.)

# Question Breakdown #
# Input: an n by n grid of distinct numbers 
# Representation: list of lists 
# Output: a list of tuples, each tuple contains the x,y-coords for each local minimum 
# Goal: Achieve with only O(n) comparisons between pairs of numbers

# Implementation idea I
# Analysis: 
