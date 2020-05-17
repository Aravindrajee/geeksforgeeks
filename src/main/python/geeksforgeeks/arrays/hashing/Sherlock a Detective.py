"""
https://practice.geeksforgeeks.org/problems/sherlock-a-detective/0
"""


def membersWithNoReportees(arr, n):
    reporteesHash = {0: 1}
    for i in range(n+1):
        reporteesHash[i] = 0
    for i in range(n):
        reporteesHash[arr[i]] += 1

    return [key for key in reporteesHash if reporteesHash[key] == 0]


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        members = membersWithNoReportees(arr, n)
        for i in members:
            print(i, end=' ')
        print()
        t -= 1
