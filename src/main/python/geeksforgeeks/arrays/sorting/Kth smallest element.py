"""
https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
"""


def kthSmallestUsingQuickSelect(arr, n, k):
    print('Implementation Pending')
    # TODO Implement the QuickSort based solution referring method 4 from
    # https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/


def kthSmallest(arr, n, k):
    arr.sort()
    return arr[k-1]


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        print(kthSmallest(arr, n, k))

        t -= 1
