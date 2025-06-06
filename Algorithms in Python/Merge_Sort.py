# Input: One n-element array of single-digit numbers, in the format of a list
# Output: the sorted version of that array
def merge_sort(array):
    n = len(array)
    # Base case:
    if n == 1:
        return array
    # Recursion Merge
    else:
        fir_halve, sec_halve = merge_sort(array[:n//2]), merge_sort(array[n//2:])
        return rec_merge(fir_halve, sec_halve)

# Input: Two sorted arrays in list format
# Output: Merged sorted array in list format

def rec_merge(arr1, arr2):
    N = len(arr1) + len(arr2)
    j, k = 0, 0
    res = []
    for i in range(N):
        if j >= len(arr1):
            res.extend(arr2[k:])
            break
        if k >= len(arr2):
            res.extend(arr1[j:])
            break
        if arr1[j] < arr2[k]:
            res.append(arr1[j])
            j += 1
        else:
            res.append(arr2[k])
            k += 1
    return res


# Test Cases
def test_case():
    array1 = [8,7,6,5,4,3,2,1]
    array2 = [5,6,7,8,4,1,2,3]
    print([1,2,3,4,5,6,7,8] == merge_sort(array1))
    print([1,2,3,4,5,6,7,8] == merge_sort(array2))
    print([2,5,8,9] == rec_merge([5,9], [2,8]))

    import random

    # Generate a 20-digit random number as a list
    def random_20_digit():
        return [random.randint(0, 9) for _ in range(20)]
    for i in range(5):
        ran = random_20_digit()
        print(merge_sort(ran) == sorted(ran)) 
if __name__ == "__main__":
    # Only runs when this file is executed directly
    print("Testing merge_sort...")
    # test cases here
    test_case()
