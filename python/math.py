def tests():
    test_cases = [[100,5050],
                  [1,1],
                  [10,55]]

    for case in test_cases:
        answer = sum_1_to_n_with_checks(case[0])
        print(case)
        print(answer, case[1], True if answer == case[1] else False)


def sum_1_to_n(n):
    """Calculates sum of values 1 to n
    n is an integer > 0
    """

    return n*(n+1)//2


def sum_1_to_n_with_checks(input):

    try:
        clean_input = int(input)
    except ValueError:
        raise TypeError

    if clean_input < 0:
        raise ValueError

    return sum_1_to_n(clean_input)

if __name__ == '__main__':
    tests()
