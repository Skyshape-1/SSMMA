### Question Statement ###
#  You are a given a unimodal array of n distinct elements , meaning that its entries are in 
#  increasing order up until its maximum element , after which its elements are in decreasing order. 
#  Give an algorithm to compute the maximum element that runs in O(log n) time.

# Breakdown:
# Input: a unimodal array of n distinct elements
# Output: maximum element of that array
# Constraint: O(log n) run time
# Assumption: Strict unimodal array, no plateaus 

# Implementation Idea I:
# 1. Mark down points on both ends of the array (start, end), indicating a segment
# 2. Mark down the midpoint of segment (mid), creating two segments
# 3. Mark down the midpoints of both segments (left, right)
# 4. Now we have five points (1, 2, 3, 4, 5) and 4 segments (a, b, c, d)
    # The five points can take different formations
    # (i) Symmetrical: 3 is largest => Eliminate segment a and b 
    # (ii) Mild skew: 4/2 is largest => Eliminate two segments on opposite side
    # (iii) heavy skew: 5/1 is largest => Eliminate three segments on opposite side
# 5. Mark down midpoints of two surviving segments and repeat the process
# Base case: if length of array is below 5, use max() to find final answer

def find_max(array):
    n = len(array)
    if n <= 5:
        return max(array)
    else:
        points = five_point(array) # Output a tuple of 5 elements
        max_ele = max(points)
        max_idx = points.index(max_ele)
        if max_idx == 0:
            return find_max(array[:n//4 + 1])
        elif max_idx == 1:
            return find_max(array[:n//2 + 1])
        elif max_idx == 2:
            return find_max(array[n//4:(n//2 + n//4 + 1)])
        elif max_idx == 3:
            return find_max(array[n//2:])
        else:
            return find_max(array[(n//2 + n//4):])

def five_point(array):
    n = len(array)
    start, end = array[0], array[-1]
    mid = array[n//2]
    left, right = array[n//4], array[n//2 + n//4]
    return [start, left, mid, right, end]

# Testing our function
P = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 10, 8, 6, 4, 2, 0]
Q = [3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 66, 74, 80, 83, 81, 75, 66, 54, 39, 21]
R = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 63, 71, 78, 84, 89, 93, 96, 98, 97, 95, 90, 82, 71, 57, 40]
print(find_max(P) == max(P))
print(find_max(Q) == max(Q))
print(find_max(R) == max(R))