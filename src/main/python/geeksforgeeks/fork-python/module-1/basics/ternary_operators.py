"""
Ternary operators also known as conditional expressions are operators that evaluate something
based on a condition being true or false.
It was added to Python in version 2.5.
"""


# Syntax: [on_true] if [expression] else [on_false]
def simple_method():
    # Program to demonstrate conditional operator
    a, b = 10, 20
    # Copy value of a in min if a < b else copy b
    min_value = a if a < b else b
    print(min_value)


def direct_method_using_tuple_dictionary_and_lambda():
    # Python program to demonstrate ternary operator
    a, b = 10, 20

    # Use tuple for selecting an item
    # (if_test_false,if_test_true)[test]
    print((b, a)[a < b])

    # Use Dictionary for selecting an item
    print({True: a, False: b}[a < b])

    # lambda is more efficient than above two methods
    # because in lambda  we are assure that
    # only one expression will be evaluated unlike in
    # tuple and Dictionary
    print((lambda: b, lambda: a)[a < b]())


def nested_if_else():
    # Python program to demonstrate nested ternary operator
    a, b = 10, 20

    print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")


'''When condition becomes true, expression [on_false]
   is not executed and value of "True and [on_true]"
   is returned.  Else value of "False or [on_false]"
   is returned.
   Note that "True and x" is equal to x. 
   And "False or x" is equal to x. 
   
   Note : The only drawback of this method is that on_true must not be zero or False. 
   If this happens on_false will be evaluated always. 
   The reason for that is if expression is true, the interpreter will check for the on_true, 
   if that will be zero or false, that will force the interpreter to check for on_false to give the final result 
   of whole expression.
   '''


# Syntax: [expression] and [on_true] or [on_false]
def hack_prior_to_2_5():
    # Program to demonstrate conditional operator
    a, b = 10, 20

    # If a is less than b, then a is assigned
    # else b is assigned (Note : it doesn't
    # work if a is 0.
    min_value = a < b and a or b

    print(min_value)


def main():
    print('Simple Method:')
    simple_method()
    print('Direct Method Using Tuple, Dictionary & Lambda')
    direct_method_using_tuple_dictionary_and_lambda()
    print('Ternary Operator as nested if-else')
    nested_if_else()
    print('Workaround to ternary operator prior to Python 2.5')
    hack_prior_to_2_5()


if __name__ == '__main__':
    main()
