def findExtra(a, b, n):
    # add code here
    low = 0
    high = n
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if mid is n - 1:
            ans = mid
            break;
        elif a[mid] == b[mid]:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1

    return ans


# {
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(findExtra(a, b, n))
# } Driver Code Ends