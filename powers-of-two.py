def powers_of_two(n):
    """
    Powers of two.
    :param n: type - int
    :return: type - list
    """
    return [2 ** power for power in range(0, n + 1)]


result = powers_of_two(4)
print(result)
