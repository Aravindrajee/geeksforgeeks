def main():
    print('Input multiple Values from 1 line')
    # input() multiple times
    x, y = input(),  input()
    print('x: ',  x)
    print('y: ', y)
    print("Looks like calling input() multiple times didn't work!!")

    # using input().split()
    print('Testing input().split() now')
    x, y = input().split()
    print('x: ', x)
    print('y: ', y)

    # Reads two numbers from input and typecasts them to int using
    # list comprehension
    print('Reads two numbers from input and typecasts them to int using list comprehension')
    x, y = [int(x) for x in input().split()]
    print('x: ', x)
    print('y: ', y)

    # Reads two numbers from input and typecasts them to int using
    # map function
    print('Reads two numbers using map() function')
    x, y = map(int, input().split())


if __name__ == '__main__':
    main()
