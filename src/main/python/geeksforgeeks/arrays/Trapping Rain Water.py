"""
https://practice.geeksforgeeks.org/problems/trapping-rain-water/0/
https://www.geeksforgeeks.org/trapping-rain-water/
"""


def maxWaterTrappedInNSquare(arr, n):
    maxWater = 0
    for i in range(n):
        max_left = arr[i]
        max_right = arr[i]
        for j in range(i):
            max_left = max(arr[j], max_left)
        for j in range(i, n):
            max_right = max(arr[j], max_right)
        maxWater += min(max_left, max_right) - arr[i]

    return maxWater


def maxWaterTrappedInLinearTimeAnd2NSpace(arr, n):
    maxWater = 0
    left = [0] * n
    right = [0] * n

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])

    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    for i in range(n):
        maxWater += min(left[i], right[i]) - arr[i]

    return maxWater


def maxWaterTrappedInLinearTimeAndJust2ExtraSpace(arr, n):
    water = 0

    left, right = 0, n-1
    left_max, right_max = 0, 0

    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] > left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
                left += 1
        else:
            if arr[right] > right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
                right -= 1

    return water


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(maxWaterTrappedInNSquare(arr, n))
        print(maxWaterTrappedInLinearTimeAnd2NSpace(arr, n))
        print(maxWaterTrappedInLinearTimeAndJust2ExtraSpace(arr, n))
        # TODO Implement the 4th method discussed in G4G
        t -= 1
