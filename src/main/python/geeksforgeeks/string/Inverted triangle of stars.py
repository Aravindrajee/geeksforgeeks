"""
https://practice.geeksforgeeks.org/problems/inverted-triangle-of-stars/0
"""


def fun_printing(n):
    for i in range(n):
        print(' '*i, '*'*(2*(n-i-1)+1), end='')


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        fun_printing(n)
        print()
        t -= 1
