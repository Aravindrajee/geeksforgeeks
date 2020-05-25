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

    print(* arr)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        fun(arr, n)
