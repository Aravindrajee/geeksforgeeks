# Python program to illustrate
# function with main


def get_integer():
    result = int(input("Enter integer: "))
    return result


def main():
    print('Started')

    output = get_integer()
    print(output)

    for step in range(output):
        print(step)


# now we are required to tell Python
# for 'Main' function existence
if __name__ == '__main__':
    main()
