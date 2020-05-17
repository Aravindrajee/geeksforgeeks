# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

# Function to create dictionary
def create_dict(arr):
    dict = {}

    # Your code here
    # Hint: use loop to iterate through arr
    # and assign key value to the dict
    for k, v in arr:
        dict[k] = v

    return dict


# {
# Driver Code Starts.
# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while (testcases > 0):
        size_arr = int(input())

        name = input().split()
        marks = input().split()
        arr = list()
        for i in range(0, size_arr, 1):
            arr.append((name[i], marks[i]))

        dict = create_dict(arr)

        for key in sorted(dict.keys()):
            print(key, dict[key])

        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends