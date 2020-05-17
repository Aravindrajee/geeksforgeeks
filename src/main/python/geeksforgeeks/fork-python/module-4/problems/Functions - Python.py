# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

##Write the function completely
def isPrime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 is 0 or number % 3 is 0:
        return False;

    i = 5
    while i * i <= number:
        if number % i is 0 or number % (i + 2) is 0:
            return False
        i += 6

    return True;


# {
# Driver Code Starts.


import math  ##You will need this for prime checking


def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        number = int(input())
        print(isPrime(number))  ##This isPrime is function that you need to create
        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends