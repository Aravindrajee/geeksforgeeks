"""
in and not in are the membership operators; used to test whether a value or variable is in a sequence.
"""


def main():
    # Examples of Membership operator
    x = 'Geeks for Geeks'
    y = {3: 'a', 4: 'b'}

    print('G' in x)

    print('geeks' not in x)

    print('Geeks' not in x)

    print(3 in y)

    print('b' in y)


if __name__ == '__main__':
    main()
