# Definition: In this file, the word "array" means a list of integers (positive)
# Note: can handle arrays with duplicates

# Input: An array of intergers in arbitrary order
# Output: The number of inversions in the array, where an inversion is 
#         a pair of indices (i, j) such that i < j and array[i] > array[j]
# Goal: To count the number of inversions in the array

# Input: An arbtrary array 
# Output: A tuple containing: (i) the sorted version of input 
#                             (ii) the number of internal inversions
def count_Inv_n_merge_sort(arrayA):
    n = len(arrayA)
    if n == 1:
        return (arrayA, 0)
    else:
        left = arrayA[:n//2]
        right = arrayA[n//2:]
        l_res, r_res = count_Inv_n_merge_sort(left), count_Inv_n_merge_sort(right)
        l_sorted, l_invs = l_res[0], l_res[1]
        r_sorted, r_invs = r_res[0], r_res[1]

        tem = count_spl_inv_n_merge(l_sorted, r_sorted)
        all_sorted, s_invs = tem[0], tem[1]
        
        return (all_sorted, s_invs + l_invs + r_invs)

# Input: two sorted arrays
# Output: merged, sorted array + the number of split invs between left and right    
def count_spl_inv_n_merge(arrayB, arrayC):
            i, j = 0, 0
            res = []
            inv_count = 0
            for k in range(len(arrayB) + len(arrayC)):
                
                if arrayB[i] <= arrayC[j]:
                    res.append(arrayB[i])
                    i += 1
                else:
                    res.append(arrayC[j])
                    j += 1
                    # Counting split inversions                 #!#
                    inv_count += (len(arrayB) - i)
                
                if i >= len(arrayB):
                    res.extend(arrayC[j:])
                    break
                if j >= len(arrayC):
                    res.extend(arrayB[i:])
                    # inv_count = inv_count + len(arrayB[i:])*len(arrayC)   #!#
                    break
            
            return (res, inv_count)

# Goal: Wrapper function 
# Input: An arbitrary array
# Output: The number of inversions
def wrapper_fun(array):
    return count_Inv_n_merge_sort(array)[1]

def primary_test_case():
    TC1 = [1,3,5,2,4,6]
    print(3 == wrapper_fun(TC1))
# primary_test_case()

def complex_test_cases():

    # Test Case 1: Reverse sorted array (maximum possible inversions)
    # In a reverse sorted array of length n, there are n*(n-1)/2 inversions
    TC1 = [5, 4, 3, 2, 1]
    expected1 = 10  # 5*(5-1)/2 = 10 inversions
    print(f"Test Case 1 (Reverse sorted): {expected1 == wrapper_fun(TC1)}")
    
    # Test Case 2: Array with repeated elements
    # This tests how the algorithm handles duplicates
    TC2 = [4, 1, 3, 4, 2, 5, 4]
    expected2 = 6  # Inversions: (4,1), (4,3), (4,2), (3,2), (4,2), (5,4), 
    print(f"Test Case 2 (With duplicates): {expected2 == wrapper_fun(TC2)}")
    
    # Test Case 3: Large array with specific pattern
    # First half ascending, second half descending - creates many split inversions
    TC3 = list(range(1, 11)) + list(range(20, 10, -1))
    expected3 = 45  # Each element in first half forms inversion with each in second half: 10*11/2 = 55
    print(f"Test Case 3 (Pattern array): {expected3 == wrapper_fun(TC3)}")
complex_test_cases()