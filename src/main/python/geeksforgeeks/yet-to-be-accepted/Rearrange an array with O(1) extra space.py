"""
https://practice.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space/0
https://www.geeksforgeeks.org/rearrange-given-array-place/
https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/
"""


def fun(arr, n):
    for i in range(n):
        arr[i] += (arr[arr[i]] %n) * n
    for i in range(n):
        arr[i] = arr[i] // n

    return ' '.join(map(str, arr))


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(fun(arr, n))
        t -= 1
