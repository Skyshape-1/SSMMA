# Input: One n-element array of single-digit numbers, in the format of a string
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

# Input: Two sorted arrays in string format
# Output: Merged sorted array in string format

def rec_merge(arr1, arr2):
    # Helper Function
    def num_lst(str):
        tem = list(str)
        return list(map(lambda dig: int(dig), tem))

    N = len(arr1) + len(arr2)
    j, k = 0, 0
    res = ""
    narr1, narr2 = num_lst(arr1), num_lst(arr2)
    for i in range(N):
        if j >= len(arr1) or k >= len(arr2):
            res = res + arr1[j:] + arr2[k:]
            break
        if narr1[j] < narr2[k]:
            res += arr1[j]
            j += 1
        else:
            res += arr2[k]
            k += 1
    return res


# Test Cases
def test_case():
    array1 = "87654321"
    array2 = "56784123"
    print("12345678" == merge_sort(array1))
    print("12345678" == merge_sort(array2))
    print("2589" == rec_merge("59", "28"))

    import random

    # Generate a 20-digit random number
    def random_20_digit():
        return ''.join([str(random.randint(0, 9)) for _ in range(20)])
    for i in range(5):
        ran = random_20_digit()
        print(merge_sort(ran) == ''.join(sorted(ran))) 

    

test_case()