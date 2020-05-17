"""
https://practice.geeksforgeeks.org/problems/ugly-numbers/0
https://www.geeksforgeeks.org/ugly-numbers/
"""


# This solution in Python will give TLE. Code the same in C/C++ to get it accepted!
def uglyNumber(n):
    ugly = [1] * n

    index_of_2 = index_of_3 = index_of_5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, n):
        ugly[i] = min(ugly[index_of_2]*2, ugly[index_of_3]*3, ugly[index_of_5]*5)
        if ugly[i] == next_multiple_of_2:
            index_of_2 += 1
            next_multiple_of_2 = ugly[index_of_2] * 2
        if ugly[i] == next_multiple_of_3:
            index_of_3 += 1
            next_multiple_of_3 = ugly[index_of_3] * 3
        if ugly[i] == next_multiple_of_5:
            index_of_5 += 1
            next_multiple_of_5 = ugly[index_of_5] * 5

    return ugly[n-1]


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        print(uglyNumber(n))
        t -= 1
