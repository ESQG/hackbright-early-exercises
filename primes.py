"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def check_divisible(number, factors):
    for j in factors:
        if number % j == 0:
            return True
        if j ** 2 > number:
            break
    return False


def primes(count):
    """Return count number of prime numbers, starting at 2."""
    ret = []
    next_number = 2
    while len(ret) < count:
        if check_divisible(next_number, ret) is False:
            ret.append(next_number)
        next_number += 1

    return ret


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
