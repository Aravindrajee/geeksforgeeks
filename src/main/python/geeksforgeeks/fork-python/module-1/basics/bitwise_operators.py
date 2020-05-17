def main():
    # Examples of Bitwise operators
    a = 10  # Binary 1010
    b = 4   # Binary 0100

    # Print bitwise AND operation
    print(a & b)

    # Print bitwise OR operation
    print(a | b)

    # Bitwise not operator: Returns one's compliment of the number.
    # Example: a = 10 = 1010 (Binary) ~a = ~1010 = -(1010 + 1) = -(1011) = -11 (Decimal)
    # Print bitwise NOT operation
    print(~a)

    # print bitwise XOR operation
    print(a ^ b)

    # print bitwise right shift operation
    print(a >> 2)

    # print bitwise left shift operation
    print(a << 2)


if __name__ == '__main__':
    main()
