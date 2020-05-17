"""
https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
"""

# Function to find the maximum contiguous subarray
from sys import maxsize


def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(maxSubArraySum(arr, n))
        t -= 1
