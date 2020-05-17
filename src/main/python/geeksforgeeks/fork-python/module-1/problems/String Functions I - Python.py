# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3


def trim(str):
    return str.strip()  # use str.strip() here to truncate all space lines


def exists(str, istr):
    return str.find(istr)  # use str.find(istr) to return 0 based index of the matched substring, else -1


def titleIt(str):
    return str.title()  # use str.title() to capitalize the first letter


def casesSwap(str):
    return str.swapcase()  # use str.swapcase() to swap the cases of lower to upper and upper to lower


# {
# Driver Code Starts.


def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        mystr = input()
        x = input()
        mystr = trim(mystr)
        print(mystr)
        print(exists(mystr, x))
        print(titleIt(mystr))
        print(casesSwap(mystr))
        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends