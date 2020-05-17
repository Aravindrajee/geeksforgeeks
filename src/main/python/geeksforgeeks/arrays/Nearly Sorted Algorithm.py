"""
https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0
https://www.geeksforgeeks.org/nearly-sorted-algorithm/
"""


def fun(arr, n):
    pass


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, k = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        arr.sort()
        for i in arr:
            print(i, end=' ')
        print()
        t -= 1
