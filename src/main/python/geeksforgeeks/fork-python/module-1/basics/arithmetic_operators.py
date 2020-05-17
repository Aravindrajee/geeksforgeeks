def atrocities_of_division_operators_in_python_2_and_3():
    print("Now Let's talk about the atrocities of division operators (/,//) in python 2.7 & python3 ")
    # A Python 2.7 program to demonstrate use of "/" for integers
    # Commenting out the code since we are running on python3
    """
    print 5 / 2         # prints 2
    print - 5 / 2       # prints -3
    #First output is fine, but the second one may be surprising if we are coming Java/C++ world. 
    In Python 2.7, the "/" operator works as a floor division for integer arguments. 
    However, the operator / returns a float value if one of the arguments is a float (this is similar to C++)
    """

    # A Python 2.7 program to demonstrate use of
    # "/" for floating point numbers
    """
    print 5.0 / 2       # prints 2.5
    print - 5.0 / 2     # prints -2.5
    """

    # A Python 2.7 program to demonstrate use of
    # "//" for both integers and floating points
    """
    print 5 // 2        # prints 2
    print - 5 // 2      # prints -3
    print 5.0 // 2      # prints 2.0
    print - 5.0 // 2    # prints -3.0
    """

    # In Python 3, '/' operator does floating point division for both int and float arguments.
    # A Python 3 program to demonstrate use of
    # "/" for both integers and floating points
    print('Python 3 / operator')
    print(5 / 2)
    print(-5 / 2)
    print(5.0 / 2)
    print(-5.0 / 2)

    # '//' operator behaves same in both python 2.7 & python 3
    print('Python 3 // operator')
    print(5 // 2)
    print(-5 // 2)
    print(5.0 // 2)
    print(-5.0 // 2)


def main():
    # Examples of Arithmetic Operator
    a = 9
    b = 4

    # Addition of numbers
    add = a + b

    # Subtraction of numbers
    sub = a - b

    # Multiplication of number
    mul = a * b

    # Division(float) of number
    div1 = a / b

    # Division(floor) of number
    div2 = a // b

    # Modulo of both number
    mod = a % b

    # Power
    p = a ** b

    # print results
    print(add)
    print(sub)
    print(mul)
    print(div1)
    print(div2)
    print(mod)
    print(p)

    atrocities_of_division_operators_in_python_2_and_3()


if __name__ == '__main__':
    main()
