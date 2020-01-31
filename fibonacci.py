#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    return some_int % 100000000


def optimized_fibonacci(n):
    """
    Optimized fibonacci returns nth fibonacci value
    :param n: integer, index of fibonacci number.
    :return: integer, fibonacci number at index n.
    """
    if n is None or type(n) == float:
        raise TypeError("Input cannot be a float or None")

    try:
        n = int(n)
    except ValueError:
        raise ValueError("The input must be a non-negative integer")

    if n < 0:
        raise ValueError("The input must be a non-negative integer")

    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


class SummableSequence(object):
    def __init__(self, *initial):  # [5, 7, 11]
        """
        initial values attached to the object
        :param initial:
        """
        initial = list(initial)

        for n in initial:
            if n is None or type(n) == float:
                raise TypeError("Input cannot be a float or None")
            try:
                n = int(n)
            except ValueError:
                raise ValueError("The input must be a non-negative integer")
            if n < 0:
                raise ValueError("The input must be a non-negative integer")

        self.initial = initial

    def __call__(self, i):  # 2, 7
        n = len(self.initial)
        if n > i:
            return self.initial[i]
        nums = self.initial[:]
        for i in range(n, i + 1):
            nums.append(sum(nums))
            nums.pop(0)
        return nums[-1]




if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
