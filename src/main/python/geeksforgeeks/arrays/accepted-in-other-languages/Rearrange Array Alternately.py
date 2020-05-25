"""
https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately/0/
https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form/
https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space/
"""


# Prints max at first position, min at second position
# second max at third position, second min at fourth position and so on
# Assumption: The provided array is already sorted in asc order!!
def rearrangeWithNSpace(arr, n):
    print('This solution should give Memory Error in GeeksForGeeks Practise,'
          ' since we are not supposed to use more than O(1) space')
    auxiliary_array = [None] * n
    small, large = 0, n-1
    for i in range(n):
        if i %2 is 0:
            auxiliary_array[i] = arr[large]
            large -= 1
        else:
            auxiliary_array[i] = arr[small]
            small += 1

    for i in auxiliary_array:
        print(i, end=' ')
    print()
    # return auxiliary_array;


# We will basically do what the package name boasts about :P
def rearrangeWithConstantExtraSpace(arr, n):
    # Get the value of biggest dude amongst them all,
    # which is basically any number gt arr[n-1] since arr is sorted in asc order
    the_big_dude = arr[n-1] + 1

    # We still need to iterate from both the ends, so we will keep 2 var, and proceed like the previous case.
    small, large = 0, n-1

    # But unlike last case, we will store the other dude at same index in same array
    for i in range(n):
        if i%2 is 0:
            arr[i] += (arr[large] % the_big_dude) * the_big_dude
            large -= 1
        else:
            arr[i] += (arr[small] % the_big_dude) * the_big_dude
            small += 1

    # Now that the parasite is home, let's kill the host
    for i in range(n):
        arr[i] //= the_big_dude

    for i in arr:
        print(i, end=' ')
    print()
    # return arr


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        rearrangeWithNSpace(arr, n)
        rearrangeWithConstantExtraSpace(arr, n)
        t -= 1
