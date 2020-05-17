import math


def main():
    num = float(input('Enter a number: '))
    absolute_value = math.fabs(num)
    print('Num:', num, 'Absolute Value:', absolute_value)


if __name__ == '__main__':
    main()