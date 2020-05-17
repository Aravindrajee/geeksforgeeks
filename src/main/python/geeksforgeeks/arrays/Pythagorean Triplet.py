"""
https://practice.geeksforgeeks.org/problems/pythagorean-triplet/0/
https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
"""


def funInNCube(arr, n):
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (arr[i] ** 2 == arr[j] ** 2 + arr[k] ** 2) \
                        or (arr[j] ** 2 == arr[i] ** 2 + arr[k] ** 2) \
                        or (arr[k] ** 2 == arr[i] ** 2 + arr[j] ** 2):
                    return "Yes"

    return "No"


def funWithSortingInNSquare(arr, n):
    arr = [x ** 2 for x in arr]
    arr.sort()

    for i in range(n - 1, 1, -1):
        j, k = 0, n - 2
        while j < k:
            if arr[i] == arr[j] + arr[k]:
                return "Yes"
            elif arr[i] > arr[j] + arr[k]:
                j += 1
            else:
                k -= 1

    return "No"


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(funInNCube(arr, n))
        print(funWithSortingInNSquare(arr, n))
        t -= 1
