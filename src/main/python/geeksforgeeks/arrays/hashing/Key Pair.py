"""
https://practice.geeksforgeeks.org/problems/key-pair/0
"""


def fun(arr, n, x):
    s = set()
    for element in arr:
        if (x-element) in s:
            return 'Yes'
        s.add(element)

    return 'No'


if __name__ == '__main__':
    for _ in range(int(input())):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        print(fun(arr, n, x))
