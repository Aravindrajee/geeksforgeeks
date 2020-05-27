"""
https://practice.geeksforgeeks.org/problems/flip-bits/0
https://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/
"""


def max_no_of_1s_possible_with_1_subarray_flip(arr, n):
    original_no_of_1s = 0

    max_so_far = -1 - 1        # -1 being the smallest number
    max_ending_here = 0
    start = end = 0
    s = 0

    for i in range(n):
        original_no_of_1s += 1 if arr[i] is 1 else 0

        max_ending_here += 1 if arr[i] is 0 else -1
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    # This needs to be printed when indices are asked
    if max_so_far > 0:
        print(start, end)

    return original_no_of_1s + max(0, max_so_far)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_no_of_1s_possible_with_1_subarray_flip(arr, n))
