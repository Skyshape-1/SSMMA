### Question Statement ###
# You are given a sorted (from smallest to largest) array A of n distinct integers which can be 
# positive, negative, or zero . You want to decide whether or not there is an index i such that 
# A[i] = i. Design the fastest algorithm that you can for solving this problem.


# Question Breakdown #
# Input: a sorted (from smallest to largest) array A of n distinct integers which can be 
#        positive, negative, or zero
# Output: a boolean, indicating whether or not there is an index i such that A[i] = i
# Goal: find the fastest possible algorithm and evalute its runtime with BigO notation
      # i.e. aim for O(n)

# Implementation idea I
# Analysis: For each element considered, there are 3 possibilities
#   1. A[i] == i
#   2. A[i] < i, all elements to the left are eliminated
#   3. A[i] > i, all elements to the right are eliminated

# Steps:
#   1. Choose midpoint of array P and evaluate accordingly
#   2. shrink the array by half
#   3. repeat Step 1 and 2 until array size = 1
#   4. return base case T/F

# Complexity 
# Time Complexity: O(log n)
# Space Complexity: O(log n)
def exist_value_equal_ind(array, start_idx = 0, end_idx = -1):
    n = len(array)
    start = start_idx
    end = n - 1 if end_idx == -1 else end_idx
    dis = end - start
    if dis == 2:
        return array[start + 1] == start + 2
    else:
        mid_idx = start + dis//2
        if array[mid_idx] == mid_idx + 1:
            return True
        cond = array[mid_idx] < mid_idx + 1
        if cond:
            start = mid_idx
        else:
            end = mid_idx

        return exist_value_equal_ind(array, start, end)

def test_case():
    P = [-4, -2, -1, 0, 1, 3, 7, 9, 12, 15, 16]
    print(exist_value_equal_ind(P)) # true
    S = [3, 4, 5, 6, 7]
    print(exist_value_equal_ind(S)) # false

test_case()
