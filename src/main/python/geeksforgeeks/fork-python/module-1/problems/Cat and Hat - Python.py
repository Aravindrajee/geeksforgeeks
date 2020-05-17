# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

def cat_hat(str):
    ##your code here##
    ##You need to write complete code this time
    cat_indices = [x for x in range(len(str)) if str.startswith('cat', x)]
    hat_indices = [x for x in range(len(str)) if str.startswith('hat', x)]
    return len(cat_indices) is len(hat_indices)


# {
# Driver Code Starts.


def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        mystr = input()
        print(cat_hat(mystr))
        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends