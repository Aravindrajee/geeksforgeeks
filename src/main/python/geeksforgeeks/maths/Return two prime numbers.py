"""
https://practice.geeksforgeeks.org/problems/return-two-prime-numbers/0
https://www.geeksforgeeks.org/find-two-prime-numbers-with-given-sum/
"""


# Python 3 program to find a prime number
# pair whose sum is equal to given number
# Python 3 program to print super primes
# less than or equal to n.

# Generate all prime numbers less than n.
def SieveOfEratosthenes(n, isPrime):
    # Initialize all entries of boolean
    # array as True. A value in isPrime[i]
    # will finally be False if i is Not a
    # prime, else True bool isPrime[n+1]
    isPrime[0] = isPrime[1] = False
    for i in range(2, n + 1):
        isPrime[i] = True

    p = 2
    while p * p <= n:

        # If isPrime[p] is not changed,
        # then it is a prime
        if isPrime[p]:

            # Update all multiples of p
            i = p * p
            while i <= n:
                isPrime[i] = False
                i += p
        p += 1


# Prints a prime pair with given sum
def findPrimePair(n):
    # Traversing all numbers to find
    # first pair
    for i in range(0, n):

        if isPrime[i] and isPrime[n - i]:
            print(i, (n - i))
            return


if __name__ == '__main__':
    # Generating primes using Sieve
    isPrime = [0] * (10000 + 1)
    SieveOfEratosthenes(10000, isPrime)

    t = int(input())
    while t > 0:
        n = int(input())
        findPrimePair(n)
        t -= 1
