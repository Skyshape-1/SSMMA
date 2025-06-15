### Question Statement ###
# You are given as input an unsorted array of n distinct numbers, where n is a power of 2. 
# Give an algorithm that identifies the second-largest number in the array, and that uses 
# at most n + log(2,n) - 2 comparisons.

# Question Breakdown #
# Input: an unsorted array of n distinct numbers , where n = 2^k, k = 1,2,3...
# Output: second-largest number in the array
# Constraint: uses at most n + log(2,n) - 2 comparisons
# Assumption: all entries in arry are positive integers

# Implementation Idea I:                                     # Constraint not met #
# Divde and conquer paradigm
# 1. Divide the array P by half (Q for left, R for right)
# 2. Recursive call to find the (sec, fir) largest element in Q, R
# 3. Compare four elements from Step 2 to produce (sec, fir) largest element in P  
    # % O(2) %

# Master Method Analysis:
# Runtime == O(n), more specifically, the worst case can take (3n/2 - 2) comparsions

P = [13, 1, 60, 7, 71, 28, 66, 2, 3, 78, 12, 33, 49, 39, 28,17] # The sec-largest element is 71

def sec_n_fir_largest(array):
    n = len(array)
    if n == 2:
        return (array[0], array[1]) if array[0] < array[1] else (array[1], array[0])
    else:
        Q, R = array[:n//2], array[n//2:]
        resQ = sec_n_fir_largest(Q)
        resR = sec_n_fir_largest(R)
        if resQ[1] < resR[1]:
            if resQ[1] < resR[0]:
                return resR
            return (resQ[1], resR[1])
        else:
            if resR[1] < resQ[0]:
                return resQ
            return (resR[1], resQ[1])

def sec_largest_only(array):
    return sec_n_fir_largest(array)[0]

print(sec_largest_only(P))


# Terminal-type Search Function #
# Optimal Solution: Tournament Method
# This method uses a tournament-style approach to find the second largest element
# This approach utilizes a tree-style iteration process
# It will at most use n + log(2,n) - 2 comparisons

def sec_largest_optimal(array):
    import math

    # Each element is paired with a list of elements it has beaten
    matches = [(num, []) for num in array]

    # Tournament to find the largest, tracking who each winner beats, at most n - 1 comparisons
    while len(matches) > 1:
        next_round = []
        for i in range(0, len(matches), 2):
            if matches[i][0] > matches[i+1][0]:
                winner, loser = matches[i], matches[i+1]
            else:
                winner, loser = matches[i+1], matches[i]
            # Winner keeps track of all it has beaten
            next_round.append((winner[0], winner[1] + [loser[0]]))
        matches = next_round

    # The only remaining element is the largest, with a list of all it beat
    largest, beaten = matches[0][0], matches[0][1]

    # The second largest is the max among the beaten elements
    second_largest = max(beaten)
    return second_largest

# Example usage:
print(sec_largest_optimal(P))