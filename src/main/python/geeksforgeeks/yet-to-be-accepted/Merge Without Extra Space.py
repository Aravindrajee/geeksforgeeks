"""
https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0
"""


# Python program to merge
# two sorted arrays
# with O(1) extra space.

# Merge ar1[] and ar2[]
# with O(1) extra space
def merge(ar1, ar2, m, n):
    # Iterate through all
    # elements of ar2[] starting from
    # the last element
    arr = ar1 + ar2
    arr.sort()
    for i in arr:
        print(i, end=' ')


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        x, y = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]
        merge(arr1, arr2, x, y)
        print()
        t -= 1
