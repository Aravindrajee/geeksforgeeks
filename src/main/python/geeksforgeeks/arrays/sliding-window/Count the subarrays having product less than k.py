"""
https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k/0
https://www.geeksforgeeks.org/number-subarrays-product-less-k/
"""


def noOfSubarrayHavingProductLtK(arr, n, k):
    count = 0
    product = 1

    start = end = 0
    while start <= end < n:
        product *= arr[end]

        while start < end and product >= k:
            product //= arr[start]
            start += 1

        if product < k:
            count += end - start + 1

        end += 1

    return count


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, k = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        print(noOfSubarrayHavingProductLtK(arr, n, k))
        t -= 1
